#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:55:22 2023

@author: hannah
"""

from owlready2 import *
import pandas as pd
import zipfile
import os
import re
import numpy as np
import types
import glob
import sys
import time

start_time = time.time()
def extract_type(query_string):
    pattern = r"\[(.*?)\]"
    match = re.search(pattern, query_string)
    return(match.group(1))

def transform_datatype(input_value):
    if type(input_value) == np.float64:
        return(float(input_value))
    if type(input_value) == np.int64:
        return(int(input_value))
    else:
        return(input_value)

accession_list = ["E-MTAB-11006", "E-CURD-5", "E-CURD-83", "E-ENAD-30", "E-ENAD-49", "E-ENAD-50", "E-MTAB-11006", 
                  "E-GEOD-121619", "E-GEOD-123013", "E-GEOD-141730", "E-GEOD-161332", "E-GEOD-152766", "E-GEOD-158761"]
# # for elem in os.listdir("/home/hannah/PythonScripts/scRNAseq/get_data/out/"):
#     accession_list.append(elem) 

uri = "ARC_00000"
uri_number = 300
# print(accession_list)
# sys.exit()

for accession in accession_list:
    print(accession)
    # accession = "E-GEOD-161332"
    isExist = os.path.exists("/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/assays/a_"+accession+"/temp/")
    if not isExist:
        os.makedirs("/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/assays/a_"+accession+"/temp/")
    
    with zipfile.ZipFile("/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/assays/a_"+accession+"/experimental_metadata.zip", "r") as zip_ref:
        zip_ref.extractall("/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/assays/a_"+accession+"/temp/")
    
    data = pd.read_csv("/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/assays/a_"+accession+"/temp/"+accession+".sdrf.txt", sep="\t")
    # data = pd.read_csv("/home/hannah/Schreibtisch/E-CURD-4.sdrf.tsv")
    
    # quality scores
    qs_path = "/home/hannah/PythonScripts/scRNAseq/get_data/out/"+accession+"/runs/r_quality/"
    scores_dict = {}
    for qs_file in glob.glob(os.path.join(qs_path, "*.txt")):
        read = qs_file.split("/")[-1][:-16] + ".fastq.gz"
        # print(read)
        # read = re.search(r"[A-Z]{3}\d{7}_\d", qs_file)[0]+".fastq.gz"
        score = -1
        with open(qs_file, "r") as f:
            score = float(f.readline())
        scores_dict[read] = score
    
    ##### Managing ontologies
    onto = get_ontology("file:///home/hannah/PythonScripts/scRNAseq/get_data/owlready2/ARC_try2_empty_reduced.owl").load()

    # sys.exit()
    
    
    
    row_index = 0
    sample_list = []
    sample_dict = {}
    for row in data.index.values:
        print(row)
        # if row_index==1:
        #     break
        col_index = 0
        sample_name = data.iloc[0][0] # [row][col]
        
        for elem in data.columns:
            tmp = None
            query = None
            cell_value = data.iloc[row_index][col_index]
            if pd.isna(cell_value):
                col_index += 1
                continue
            
            instance_uri = uri + str(uri_number)
            cell_value = transform_datatype(cell_value)
            instance_label = str(cell_value)
            instance_exists = None


            
            if "Source Name" in elem:
                s1 = onto.ARC_00000070(instance_uri, namespace=onto, is_a=[onto.ARC_00000070], label=cell_value)
                # sample_list.append(s1)
                sample_dict[s1] = None
                
            elif "Comment" in elem:
                tmp = extract_type(elem)
                class_exists = onto.search(label = tmp)
                new_class = None
                new_prop = None
                instance_exists = onto.search(label = instance_label)
                new_instance = None
                
                if class_exists != []:
                    new_class = class_exists[0]
                    new_class.is_a.append(onto.ARC_00000017)
                else:
                    # creating a new class if class label doesn't exist yet
                    new_uri = uri + str(uri_number + 1)
                    with onto:
                        NewClass = types.new_class(new_uri,(onto.ARC_00000017,))
                        NewClass.label = tmp
                        NewClass.creator = "Hannah Doerpholz"
                    uri_number += 1
                    new_class = NewClass
                    
                
                ie = dict.fromkeys(instance_exists, None)
                keys_to_remove = [key for key in ie if key in sample_dict]
                for key in keys_to_remove:
                    instance_exists.remove(key)
                # # print(instance_exists)
                # # tag = "-"
                # for sample in sample_list:
                #     # print("SAMPLE",sample, "vs", instance_exists)
                #     if sample in instance_exists:
                #         # print("is a sample")
                #         # tag = "s"
                #         instance_exists.remove(sample)
                #     # else:
                #     #     tag = "n"
                
                # print("after removing", instance_exists)
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(new_class)
                else:
                    # print("new instance found", instance_label)
                    # new_instance = instance_label
                    new_instance = new_class(instance_uri, namespace=onto, is_a=[new_class], label = instance_label)
                    # print(new_instance.label, new_instance)
                    new_instance.ARC_00000036.append(cell_value)
        
                            
                for x in onto.object_properties():
                    if tmp in x.label[0]:
                        new_prop = x
                        break
                if new_prop == None:
                    prop_uri = uri + str(uri_number + 1)
                    with onto:
                        NewProp = types.new_class(prop_uri, (ObjectProperty,))
                        NewProp.label = "has " + tmp
                        NewProp.domain = [onto.ARC_00000070]
                        NewProp.range = [new_class]
                    uri_number += 1
                    new_prop = NewProp
                do_string = "s1." + new_prop.name + ".append(new_instance)" 
                exec(do_string)
                # print("\n")
                
            elif "Characteristic" in elem:
                tmp = extract_type(elem)
                class_exists = onto.search(label = tmp)
                new_class = None
                new_prop = None
                instance_exists = onto.search(label = instance_label)
                new_instance = None
                
                if class_exists != []:
                    new_class = class_exists[0]
                    new_class.is_a.append(onto.ARC_00000079)
                else:
                    # creating a new class if class label doesn't exist yet
                    new_uri = uri + str(uri_number + 1)
                    with onto:
                        NewClass = types.new_class(new_uri,(onto.ARC_00000079,))
                        NewClass.label = tmp
                        NewClass.creator = "Hannah Doerpholz"
                    uri_number += 1
                    new_class = NewClass
                
                
                ie = dict.fromkeys(instance_exists, None)
                keys_to_remove = [key for key in ie if key in sample_dict]
                for key in keys_to_remove:
                    instance_exists.remove(key)
                # # print(instance_exists)
                # # tag = "-"
                # for sample in sample_list:
                #     # print("SAMPLE",sample, "vs", instance_exists)
                #     if sample in instance_exists:
                #         # print("is a sample")
                #         # tag = "s"
                #         instance_exists.remove(sample)
                #     # else:
                #     #     tag = "n"
                
                # print(instance_exists, tag)
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(new_class)
                else:
                    # print("new instance found", instance_label)
                    # new_instance = instance_label
                    new_instance = new_class(instance_uri, namespace=onto, is_a=[new_class], label = instance_label)
                    # print(new_instance.label, new_instance)
                    new_instance.ARC_00000036.append(cell_value)
                
                # if instance_exists != []:
                #     new_instance = instance_exists[0]
                #     new_instance.is_a.append(new_class)
                # else:
                #     new_instance = instance_label
                #     new_instance = new_class(instance_uri, namespace=onto, is_a=[new_class], label = instance_label)
                #     new_instance.ARC_00000036.append(cell_value)
                            
                for x in onto.object_properties():
                    if tmp in x.label[0]:
                        new_prop = x
                        break
                if new_prop == None:
                    prop_uri = uri + str(uri_number + 1)
                    with onto:
                        NewProp = types.new_class(prop_uri, (ObjectProperty,))
                        NewProp.label = "has " + tmp
                        NewProp.domain = [onto.ARC_00000070]
                        NewProp.range = [new_class]
                    uri_number += 1
                    new_prop = NewProp
                do_string = "s1." + new_prop.name + ".append(new_instance)" 
                exec(do_string)
    
            elif "Unit" in elem:
                tmp = str(data.iloc[row_index][col_index-1])
                instance_exists = onto.search(label = instance_label)
                new_instance = ""
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000105)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000105(instance_uri, namespace=onto, is_a=[onto.ARC_00000105], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                
                related_instance = onto.search(label = tmp)[0]
                related_instance.ARC_00000106.append(new_instance)
                
            elif "Material Type" in elem:
                # print("\n")
                instance_exists = list(onto.search(label = instance_label))#, type = [onto.ARC_00000142])
                new_instance = ""
                
                
                class_set = set(onto.classes())
                ie = set(instance_exists)
                common_entities = ie & class_set
                instance_exists = [entity for entity in instance_exists if entity not in common_entities]
                
                
                # class_list = []
                # # class_dict = {}
    
                # a = onto.classes()
                # for c in a:
                #     # class_dict[c] = None
                #     class_list.append(c)
                # print(len(instance_exists), len(class_list))
                # for entity in instance_exists:
                #     if entity in class_list:
                #         # tag = "f"
                #         instance_exists.remove(entity)
                
                if instance_exists != []:# and tag != "f":
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000142)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000142(instance_uri, namespace=onto, is_a=[onto.ARC_00000142], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000143.append(new_instance)
                
            elif "Protocol REF" in elem:
                instance_exists = onto.search(label = instance_label, type = [onto.ARC_00000040])
                new_instance = ""
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000040)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000040(instance_uri, namespace=onto, is_a=[onto.ARC_00000040], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000039.append(new_instance)
                
            elif "Term Source REF" in elem:
                pass
            
            elif "Extract Name" in elem:
                instance_exists = list(onto.search(label = instance_label))
                new_instance = ""
                # print(instance_exists)
                
                ie = dict.fromkeys(instance_exists, None)
                keys_to_remove = [key for key in ie if key in sample_dict]
                for key in keys_to_remove:
                    instance_exists.remove(key)               
                # # tag = "-"
                # for sample in sample_list:
                #     # print("SAMPLE",sample, "vs", instance_exists)
                #     if sample in instance_exists:
                #         # print("is a sample")
                #         # tag = "s"
                #         instance_exists.remove(sample)
                #     # else:
                #     #     tag = "n"
                
                # print(instance_exists, tag)
                if instance_exists != []:# and tag == "n":
                    # print("instance exists", instance_exists[1].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000147)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000147(instance_uri, namespace=onto, is_a=[onto.ARC_00000147], label = instance_label)
                    # print(new_instance.label, new_instance)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000148.append(new_instance)
                # print(s1.ARC_00000148)
                # print("\n")
                
            elif "Assay Name" in elem:
                # print(instance_label)
                instance_exists = list(onto.search(label = instance_label))
                new_instance = ""
                # print(instance_exists)
                
                ie = dict.fromkeys(instance_exists, None)
                keys_to_remove = [key for key in ie if key in sample_dict]
                for key in keys_to_remove:
                    instance_exists.remove(key)
                # # tag = "-"
                # for sample in sample_list:
                #     # print("SAMPLE", sample, "vs", instance_exists)
                #     if sample in instance_exists:
                #         # print("is a sample")
                #         # tag = "s"
                #         instance_exists.remove(sample)
                #     # else:
                #     #     tag = "n"
                
                # print(instance_exists, tag)
                if instance_exists != []:# and tag == "n":
                    # print("instance exists", instance_exists[0].label, instance_exists[0])
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000196)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000196(instance_uri, namespace=onto, is_a=[onto.ARC_00000196], label = instance_label)
                    # print(new_instance.label, new_instance)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000197.append(new_instance)
                # print(s1.ARC_00000197)
                # print("\n")
                
            elif "Technology Type" in elem:
                instance_exists = onto.search(label = instance_label)
                new_instance = ""
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000068)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000068(instance_uri, namespace=onto, is_a=[onto.ARC_00000068], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000072.append(new_instance)
                
            elif "Scan Name" in elem:
                instance_exists = onto.search(label = instance_label)
                new_instance = ""
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000054)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000054(instance_uri, namespace=onto, is_a=[onto.ARC_00000054], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000206.append(new_instance)
                
            elif "Factor Value" in elem:
                tmp = extract_type(elem)
                class_exists = onto.search(label = tmp)
                new_class = None
                new_prop = "ARC_00000043"
                instance_exists = onto.search(label = instance_label)
                new_instance = None
                
                if class_exists != []:
                    new_class = class_exists[0]
                    new_class.is_a.append(onto.ARC_00000084)
                else:
                    # creating a new class if class label doesn't exist yet
                    new_uri = uri + str(uri_number + 1)
                    with onto:
                        NewClass = types.new_class(new_uri,(onto.ARC_00000084,))
                        NewClass.label = tmp
                        NewClass.creator = "Hannah Doerpholz"
                    uri_number += 1
                    new_class = NewClass
                
                if instance_exists != []:
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(new_class)
                else:
                    new_instance = instance_label
                    new_instance = new_class(instance_uri, namespace=onto, is_a=[new_class], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                            
                do_string = "s1." + new_prop + ".append(new_instance)" 
                exec(do_string)
            
            elif "Performer" in elem:
                instance_exists = onto.search(label = instance_label)
                new_instance = ""
                if instance_exists != []:
                    # print("instance exists", instance_exists[0].label)
                    new_instance = instance_exists[0]
                    new_instance.is_a.append(onto.ARC_00000081)
                else:
                    # print("new instance found", instance_label)
                    new_instance = onto.ARC_00000081(instance_uri, namespace=onto, is_a=[onto.ARC_00000081], label = instance_label)
                    new_instance.ARC_00000036.append(cell_value)
                s1.ARC_00000112.append(new_instance)
                   
    
            uri_number += 1
            col_index += 1    
        row_index += 1
    
    
    # scored_read_file_URI = onto.search(label = "read1 file")
    # if scored_read_file_URI != []:
    #     scored_read_file = onto.search(type = scored_read_file_URI[0])
    #     for elem in scored_read_file:
    #         key = elem.ARC_00000036[0]
    #         elem.ARC_00000073.append(scores_dict[key])
    #         plot_file_path = qs_path + elem.ARC_00000036[0].split(".")[0] + "_fastqc_radarplot.png"
    #         elem.ARC_00000069.append(plot_file_path)
    
    
    # scored_read_file_URI2 = onto.search(label = "read2 file")
    # if scored_read_file_URI2 != []:
    #     scored_read_file2 = onto.search(type = scored_read_file_URI2[0])
    #     for elem in scored_read_file2:
    #         key = elem.ARC_00000036[0]
    #         elem.ARC_00000073.append(scores_dict[key])
    #         plot_file_path2 = qs_path + elem.ARC_00000036[0].split(".")[0] + "_fastqc_radarplot.png"
    #         elem.ARC_00000069.append(plot_file_path)
        
    # scored_read_file_URI3 = onto.search(label = "index1 file")
    # if scored_read_file_URI3 != []:
    #     scored_read_file3 = onto.search(type = scored_read_file_URI3[0])
    #     for elem in scored_read_file3:
    #         key = elem.ARC_00000036[0]
    #         elem.ARC_00000073.append(scores_dict[key])
    #         plot_file_path3 = qs_path + elem.ARC_00000036[0].split(".")[0] + "_fastqc_radarplot.png"
    #         elem.ARC_00000069.append(plot_file_path)
    
    
    ENA_RUN_class = onto.search(label = "ENA_RUN")
    FASTQ_URI_class = onto.search(label = "FASTQ_URI")
    success = False
    
    if FASTQ_URI_class != []:
        print("fastq using")
        FTP_files = onto.search(type = FASTQ_URI_class)
        for elem in FTP_files:
            try:
                key = elem.ARC_00000036[0].split("/")[-1]
                # print(key)
                elem.ARC_00000073.append(scores_dict[key])
                plot_file_path_ftp = qs_path + elem.ARC_00000036[0].split(".")[0] + "_fastqc_radarplot.png"
                elem.ARC_00000069.append(plot_file_path_ftp)
                success = True
            except:
                pass
                # print("FASTQ key not in dictionary!!!")
    if ENA_RUN_class != [] and success == False:
        print("ena using")
        FTP_files = onto.search(type = ENA_RUN_class)
        for elem in FTP_files:
            try:
                key = elem.ARC_00000036[0] + ".fastq.gz"
                # print(key)
                elem.ARC_00000073.append(scores_dict[key])
                plot_file_path_ftp = qs_path + elem.ARC_00000036[0].split(".")[0] + "_fastqc_radarplot.png"
                elem.ARC_00000069.append(plot_file_path_ftp)
                success = True
            except:
                pass
                # print("RUN key not in dictionary!!!")
    
    if success == False:
        print("files are not referenced in metadata")

    
    

            
onto.save(file = "/home/hannah/PythonScripts/scRNAseq/get_data/owlready2/fill_reduced_ARC_ontology_slow_v1.owl", format="rdfxml")
end_time = time.time()
print("add data slow", end_time-start_time)




        
        
        
        