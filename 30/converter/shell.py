#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:05:32 2022

@author: hannah
"""

import requests
from bs4 import BeautifulSoup
import re
import ast
import pandas as pd
import os
# import time
from datetime import date
from csv import reader, DictWriter, writer
# import lxml
# import json
import zipfile
import shutil
import logging
import mapping_dict as mp
import isa
import sys
import subprocess

'''
Python version: 3.10
'''

###########################
def check_yes_no_to_true_false(text):
    while True:
        try:
            answer = input(text)
        except ValueError:
            print("I'm afraid your answer was invalid.")
            continue
        
        
        if answer == "y" or answer == "Y":
            # print("confirmed download\n")
            return True
        elif answer == "n" or answer == "N":
            # print("confirmed download rejection\n")
            return False
        elif answer != "y" or answer != "Y" or answer != "n" or answer != "N":
            print("Your answer was invalid. Please put in (y/n) as your answer.\n")
            continue
        else:
            print("FATAL ERROR OCCURED IN INPUT VALIDATION.")
            break

###########################
def dictionary_list_items(element, dictionary):
    length = len(dictionary["Investigation Title"])
    item = [""] * length
    item[0] = element
    return item

###########################
def response_status(r, url, function_name="response_status"):
    if (r.status_code >= 100 and r.status_code <200):
        print(f"[WARNING] {r.status_code} information in {function_name} on link {url}")
        logging.warning(f"{r.status_code} information in {function_name} on link {url}")
    elif (r.status_code >= 200 and r.status_code <300):
        print(f"[INFO] {r.status_code} success in {function_name} on link {url}")
        logging.info(f"{r.status_code} success in {function_name} on link {url}")
    elif (r.status_code >= 300 and r.status_code <400):
        print(f"[WARNING] {r.status_code} redirect in {function_name} on link {url}")
        logging.warning(f"{r.status_code} redirect in {function_name} on link {url}")
    elif (r.status_code >= 400 and r.status_code <500):
        if r.status_code == 404:
            print(f"[ERROR] 404 Error in {function_name}: Unlucky. Looks like the link doesn't exist. You tried to access the following website: {url}"
                  "\nIf you have checked that the link is correct, consider opening an issue to get support for that site.")
            logging.error(f"404 Error in {function_name}: Unlucky. Looks like the link doesn't exist. You tried to access the following website: {url}"
                  "\nIf you have checked that the link is correct, consider opening an issue to get support for that site.")
        else:
            print(f"[ERROR] {r.status_code} client error in {function_name} on link {url}")
            logging.error(f"{r.status_code} client error in {function_name} on link {url}")
    elif (r.status_code >= 500 and r.status_code <600):
        print(f"[ERROR] {r.status_code} server error in {function_name} on link {url}")
        logging.error(f"{r.status_code} server error in {function_name} on link {url}")
    else:
        print(f"[ERROR] {r.status_code} unknown error in {function_name} on link {url}")
        logging.error(f"{r.status_code} unknown error in {function_name} on link {url}")
    return r.status_code

###########################
def get_basics(dictionary, scExpressionAtlasAccession):
    # download basic info: title, publication, organism, number of cells, pubmed link
    url = "https://www.ebi.ac.uk/gxa/sc/experiments/"+scExpressionAtlasAccession+"/results/tsne"
    r = requests.get(url, allow_redirects=True)
    response_stat = response_status(r, url, get_basics.__name__)
    if response_stat >= 200 and response_stat < 300:
        r_text = r.text
        soup = BeautifulSoup(r_text, "html.parser")
        # get different information required by ISA as well as ExpressionAtlas specific ones
        # MAGEtab: experiment_title = soup.find(id="goto-experiment").contents[0].strip()
        organism = soup.find(id="experimentOrganisms").find("span").text
        number_of_cells = int(soup.find("div", id="experimentDescription").find("div", class_="media-object-section middle").find("div").text.split(": ")[1].replace(",", ""))
        dictionary["Comment[organism]"] = dictionary_list_items(organism, dictionary)
        dictionary["Comment[number of cells]"] = dictionary_list_items(number_of_cells, dictionary)
        print("[INFO] download of basic information done")
    else:
        print("[WARNING] no basic information could be downloaded")
    return dictionary
     
###########################
def get_experiment(dictionary, scExpressionAtlasAccession, arc_paths, experiment_design=False, experiment_metadata=False):
    # download experiment design
    if experiment_design == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download?fileType=experiment-design&accessKey="
        r = requests.get(url, allow_redirects=True)
        response_stat = response_status(r, url, get_experiment.__name__)
        if response_stat >= 200 and response_stat < 300:
            r_text = r.text
            open(arc_paths[0]+"experimental_design.tsv","w").write(r_text)
            print("[INFO] download of experiment design file done")
        else:
            print("[WARNING] no experiment design file could be downloaded")
        
        # print(dictionary["Comment[SecondaryAccession]"])
    # download experiment metadata
    if experiment_metadata == True:
        url="https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=experiment-metadata&accessKey="
        r = requests.get(url, allow_redirects=True)
        response_stat = response_status(r, url, get_experiment.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(arc_paths[1]+"experimental_metadata.zip","wb").write(r.content)
            with zipfile.ZipFile(arc_paths[1]+"experimental_metadata.zip", "r") as zip_ref:
                zip_ref.extractall(temp)
            with open(temp+scExpressionAtlasAccession+".idf.txt", "r") as f:
                file_reader = reader(f, delimiter="\t")
                for row in file_reader:
                    dictionary[row[0]] = row[1:]
            shutil.rmtree(temp)
            dictionary["Study Identifier"] = dictionary_list_items(arc_paths[0].split("/")[4], dictionary)
            dictionary["Study File Name"] = dictionary_list_items("studies" + arc_paths[0].split("studies")[1] + "isa.study.xlsx", dictionary)
            if not "Investigation Accession" in dictionary:
                dictionary["Investigation Accession"] = dictionary_list_items("i_" + scExpressionAtlasAccession, dictionary)
            print("[INFO] download of experimental metadata zip archive done")
        else:
            print("[WARNING] no experiment metadata information could be downloaded")
    return dictionary

###########################
def get_ontology_description(dictionary):
    # get ontology description from EBI ontology lookup service
    ontology_descriptions = []
    if "Term Source Name" in dictionary:
        for elem in dictionary["Term Source Name"]:
            if elem == "ArrayExpress" or elem == "":
                ontology_descriptions.append("")
                continue
            if elem == "NCBI Taxonomy":
                elem = "NCBITaxon"
            url = "https://www.ebi.ac.uk/ols/api/ontologies/"+elem
            r = requests.get(url, allow_redirects=True)
            response_stat = response_status(r, url, get_ontology_description.__name__)
            if response_stat >= 200 and response_stat < 300:
                data = r.json()
                ontology_description = data["config"]["description"]
                ontology_descriptions.append(ontology_description)
                print("[INFO] download of ontology description done")
            else:
                print("[WARNING] no ontology description could be downloaded")
        dictionary["Term Source Description"] = ontology_descriptions
    return dictionary

###########################
def get_results(scExpressionAtlasAccession, arc_path, clustering=False, marker_genes=False, normalized_counts=False, raw_counts=False, filtered_TPMs=False):
    # download result files
    if clustering == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download?fileType=cluster&accessKey="
        r = requests.get(url)
        response_stat = response_status(r, url, get_results.__name__)
        if response_stat >= 200 and response_stat < 300:
            r_text = r.text
            open(arc_path+"clustering_file.tsv", "w").write(r_text)
            print("[INFO] download of clustering file done")
        else:
            print("[WARNING] no clustering file could be downloaded")
        
    if marker_genes == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=marker-genes&accessKey="
        r = requests.get(url)
        response_stat = response_status(r, url, get_results.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(arc_path+"marker_gene_files.zip", "wb").write(r.content)
            print("[INFO] download of marker gene files zip archive done")
        else:
            print("[WARNING] no marker gene archive could be downloaded")
        
    if normalized_counts == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=normalised&accessKey="
        r = requests.get(url)
        response_stat = response_status(r, url, get_results.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(arc_path+"normalized_counts_files.zip", "wb").write(r.content)
            print("[INFO] download of normalized counts files zip archive done")
        else:
            print("[WARNING] no normalized count archive could be downloaded")
        
    if raw_counts == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=quantification-raw&accessKey="
        r = requests.get(url)
        response_stat = response_status(r, url, get_results.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(arc_path+"raw_counts_files.zip", "wb").write(r.content)
            print("[INFO] download of raw counts files zip archive done")
        else:
            print("[WARNING] no raw counts archive could be downloaded")
          
    if filtered_TPMs == True:
        url = "https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=quantification-filtered&accessKey="
        r = requests.get(url)
        response_stat = response_status(r, url, get_results.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(arc_path+"filtered_TPMs_files.zip", "wb").write(r.content)
            print("[INFO] download of filtered TMPs files zip archive done")
        else:
            print("[WARNING] no filtered TPMs archive could be downloaded")
        
###########################
def get_analysis_methods(scExpressionAtlasAccession, arc_path):
    # download supplementary information aka analysis tool info
    url = "https://www.ebi.ac.uk/gxa/sc/experiments/"+scExpressionAtlasAccession+"/supplementary-information"
    r = requests.get(url, allow_redirects=True)
    response_stat = response_status(r, url, get_analysis_methods.__name__)
    if response_stat >= 200 and response_stat < 300:
        soup = BeautifulSoup(r.text, "html.parser")
        child_soup = list(ast.literal_eval(str(soup.find_all("script")[3]).split("\"Analysis Methods\",\"props\":{\"data\":[")[1].split("]}},{\"type\":\"resources\"")[0]))
        analysis_methods_df = pd.DataFrame(child_soup[1:], columns = [child_soup[0]])
        analysis_methods_df.to_csv(arc_path+"analysis_methods.tsv", sep="\t", index=False)
        print("[INFO] download of analysis methods done")
    else:
        print("[WARNING] no analysis methods information could be downloaded")

###########################
def generate_arc_filestructure(arc_paths):
    for elem in arc_paths:
        isExists = os.path.exists(elem)
        if not isExists:
            os.makedirs(elem)
    

###########################
def create_investigation_xlsx(dictionary, single_file=True, path=None, arc_p=None):
    investigation = isa.INVESTIGATION
    for key in dictionary.keys():
        if key in mp.idf_to_isa_investigation.keys():
            investigation[mp.idf_to_isa_investigation[key]] = dictionary[key]
    investigation = pd.DataFrame.from_dict(investigation).transpose()
    if single_file == True:
        investigation.to_csv(path+"isa.investigation.xlsx", header=False, sep="\t")
    else:
        study = create_study_xlsx(dictionary, arc_path=arc_p[0], single_file=True)
        # investigation = investigation.append(study)
        investigation = pd.concat([investigation, study])
        
        investigation.to_csv(path+"isa.investigation.xlsx", header=False, sep="\t")
        create_assay_xlsx(dictionary, arc_path=arc_p[1], single_file=True)
    return investigation
        
def create_study_xlsx(dictionary, arc_path=None, single_file=True):
    study = isa.STUDY
    for key in dictionary.keys():
        if key in mp.idf_to_isa_study.keys():
            study[mp.idf_to_isa_study[key]] = dictionary[key]
        elif key not in mp.idf_to_isa_investigation.keys():
            study[key] = dictionary[key]
    study = pd.DataFrame.from_dict(study).transpose()
    if single_file == True:
        study.to_csv(arc_path+"isa.study.xlsx", header=False, sep="\t")
    return study

def create_assay_xlsx(dictionary, arc_path, single_file=True):
    assay = isa.ASSAY_METADATA
    for key in dictionary.keys():
        if key in mp.idf_to_isa_assay.keys():
            assay[mp.idf_to_isa_assay[key]] = dictionary[key]
    if single_file == True:
        assay = pd.DataFrame.from_dict(assay).transpose()
        assay.to_csv(arc_path+"isa.assay.xlsx", header=False, sep="\t")
    else:
        pass

def cleanup(dictionary):
    for key in list(dictionary):
        if key == "":
            del dictionary[key]
    return dictionary

def make_paths():
    input_scEA = input("\nWelcome to the scEA2ARC converter! This converter helps you download and structure metadata "
          "from the single cell Expression Atlas from EBI into a DataPLANT ARC, as well as download "
          "the experimental data. Please enter a scEA accession below and press enter:\n\n")
    # scEA_investigations = ["E-MTAB-11006", "E-GEOD-152766", "E-CURD-83", "E-GEOD-141730", "E-ENAD-50", "E-ENAD-49", "E-GEOD-158761", 
                            #"E-GEOD-161332", "E-GEOD-123013", "E-GEOD-121619", "E-CURD-5", "E-CURD-4", "E-ENAD-30"]
    # scExpressionAtlasAccession = "E-GEOD-152766"
    # scExpressionAtlasAccession = "E-MTAB-11006"
    path = "./out/" + input_scEA + "/"
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
    temp = path+"tmp/"
    isExists = os.path.exists(temp)
    if not isExists:
        os.makedirs(temp)
    log = path+"log/"
    isExists = os.path.exists(log)
    if not isExists:
        os.makedirs(log)
        
    arc_paths = [path + "studies/s_" + input_scEA + "/", path + "studies/s_" + input_scEA + "/protocol/", 
                 path + "studies/s_" + input_scEA + "/resources/", path + "assays/a_" + input_scEA + "/", 
                 path + "assays/a_" + input_scEA + "/dataset/", path + "assays/a_" + input_scEA + "/protocol/",
                 path + "runs/r_" + input_scEA + "/", path + "workflows/w_" + input_scEA + "/"]
    return path, temp, log, arc_paths, input_scEA






    


###########################
if __name__ == "__main__":
    # INPUT
    interactive = 1
    sys.tracebacklimit = 0
    # user_input_scEA = input("\nWelcome to the scEA2ARC converter! This converter helps you download and structure metadata "
    #       "from the single cell Expression Atlas from EBI into a DataPLANT ARC, as well as download "
    #       "the experimental data. Please enter a scEA accession below and press enter:\n\n")
    # # scEA_investigations = ["E-MTAB-11006", "E-GEOD-152766", "E-CURD-83", "E-GEOD-141730", "E-ENAD-50", "E-ENAD-49", "E-GEOD-158761", 
    #                         #"E-GEOD-161332", "E-GEOD-123013", "E-GEOD-121619", "E-CURD-5", "E-CURD-4", "E-ENAD-30"]
    # # scExpressionAtlasAccession = "E-GEOD-152766"
    # # scExpressionAtlasAccession = "E-MTAB-11006"
    # path = "./out/" + user_input_scEA + "/"
    # isExists = os.path.exists(path)
    # if not isExists:
    #     os.makedirs(path)
    # temp = path+"tmp/"
    # isExists = os.path.exists(temp)
    # if not isExists:
    #     os.makedirs(temp)
    # log = path+"log/"
    # isExists = os.path.exists(log)
    # if not isExists:
    #     os.makedirs(log)
        
    # arc_paths = [path + "studies/s_" + user_input_scEA + "/", path + "assays/a_" + user_input_scEA + "/", path + "runs/r_" + user_input_scEA + "/", path + "workflows/w_" + user_input_scEA + "/"]
    path, temp, log, arc_paths, user_input_scEA = make_paths()
    
        
    # test="ERP132245"

    # # get today's date
    # today = str(date.today())
    
    # OUTPUT
    out_dict = {}
    ena_links = {}
    logging.basicConfig(filename=log+"logfile.log", encoding='utf-8', level=logging.DEBUG)
    
    # RUN THE CODE IN SHORT
    if interactive == 0:
        generate_arc_filestructure(arc_paths)
        get_experiment(out_dict, user_input_scEA, arc_paths, experiment_design=False, experiment_metadata=True)
        get_basics(out_dict, user_input_scEA)
        get_results(user_input_scEA, arc_paths[2], clustering=False, marker_genes=False, normalized_counts=False, raw_counts=False, filtered_TPMs=False)
        get_analysis_methods(user_input_scEA, arc_paths[3])
        get_ontology_description(out_dict)
        cleanup(out_dict)
        create_investigation_xlsx(out_dict, single_file=False, path=path, arc_p=arc_paths)
        subprocess.run(["chmod", "775", "-R", path])

        
        
        
        
        
        
        
        
        
        
    
   
    
    # RUN THE CODE
    else:
        generate_arc_filestructure(arc_paths)
        answer1 = check_yes_no_to_true_false("\nYour ARC file structure has been created. You may now choose "
                                            "whether you want to download the table containing the experimental "
                                            "design. This will in the future be replaced by converting this "
                                            "table into an assay table and added to the isa.study.xlsx. Would "
                                            "you like do download this table (y/n)?\n")
        get_experiment(out_dict, user_input_scEA, arc_paths, experiment_design=answer1, experiment_metadata=True)
        get_basics(out_dict, user_input_scEA)
        print("\nThe basic metadata information on your study of interest has been collected. If you downloaded "
              "the experimenal design file, you can find this in the studies folder of the ARC.")
        answer2 = check_yes_no_to_true_false("\nYou may now choose whether you want to download the "
                                              "result files. Depending on the study, multiple different files "
                                              "may be availabe. Do you want to download the clustering file "
                                              "(y/n)?\n")
        answer3 = check_yes_no_to_true_false("\nDo you want to download the marker gene files (y/n)?\n")
        answer4 = check_yes_no_to_true_false("\nDo you want to download the normalized counts files (y/n)?\n")
        answer5 = check_yes_no_to_true_false("\nDo you want to download the raw counts files (y/n)?\n")
        answer6 = check_yes_no_to_true_false("\nDo you want to download the filtered TPMs files (y/n)?\n")
        get_results(user_input_scEA, arc_paths[2], clustering=answer2, marker_genes=answer3, normalized_counts=answer4, raw_counts=answer5, filtered_TPMs=answer6)
        print("The chosen result files of your study of interest have been downloaded. They can be found "
              "in the runs folder of the ARC.")
        get_analysis_methods(user_input_scEA, arc_paths[3])
        print("The analysis methods table has been downloaded and added to the workflows folder of the ARC.")
        get_ontology_description(out_dict)
        print("\nNow the respectiva ISA files are generated. You will find the isa.investigation.xlsx in the "
              "root of your ARC, the isa.study.xlsx can be found in the respective folder in the studies "
              "directory, the isa.assay.xlsx can be found in the respective folder in the assays directory.")
        cleanup(out_dict)
        create_investigation_xlsx(out_dict, single_file=False, path=path, arc_p=arc_paths)
        #create_study_xlsx(out_dict, arc_paths[0], single_file=True)
        #create_assay_xlsx(out_dict, arc_paths[1], single_file=True)
        
        subprocess.run(["chmod", "775", "-R", path])
        
        
        
        # os.system(bash_command)
        print("\nThank you for using the scEA2ARC! For feedback please visit the Github")
        
        
        # if out_dict["Comment[SecondaryAccession]"]:
        #     external_accessions_list = list(filter(None, out_dict["Comment[SecondaryAccession]"]))
        #     for external_accession in external_accessions_list:
        #         validity = ed.get_secondary_accession_validity(external_accession)
        #         if validity == "valid":
        #             ena_links = ed.get_ena_study_info(external_accession, ena_links)
        #             if ena_links["ENA-SAMPLE"]:
        #                 ed.get_ena_sample_info(ena_links["ENA-SAMPLE"])
        
        
        # print("\nOUTPUT")
        # for key in out_dict.keys():
        #     print(key)


















#------------------------------------------------------------------------------------------------------------------------------
# OLD CODE
# old, less sophisticated code version to get organism, number_of_cells and pubmed_url
# organism = soup.find(id="experimentOrganisms").find().text.strip()
# organism = organism.split(":")[1].strip()
# old, less sophisticated version to get the number_of_cells
# number_of_cells = None
# cell_number_div_search = soup.find_all("div")
# for element in cell_number_div_search:
#     search = element.text
#     pattern = re.compile("Number of cells: \d+")
#     match_result = pattern.match(search)
#     if match_result != None:
#         number_of_cells = int(match_result.group(0).split(": ")[1])
# old, less sophisticated version to get the pubmed url
# pubmed_url = str(soup.find(id="experimentReferences").contents[1])
# pattern = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
# pubmed_id = re.findall(pattern, pubmed_url)[0]
# pubmed_url = str(pubmed_id[0:1])[2:-3]
# pubs = soup.find(id="experimentReferences").text.strip()
# pubs = pubs.replace("\n"," ").split(":")[1].strip()
# publications = {}
# for element in pubs:
#     element = re.sub(r"(\))", "):", pubs).split(":")
#     publications[element[0]] = element[1].strip()
# metapub package utils
# fetch = PubMedFetcher()
# article = fetch.article_by_pmid(pubmed_id)
# publication_title = article.title
# publication_authors = "; ".join(article.authors)
# publication_doi = article.citation.split("doi: ")[1]



# # try to access the original ENA entry as well for more descriptions
# # all labeled "investigation" here might be study, investigation can be project from ENA
# base_info["Investigation Title"] = experiment_title
# base_info["Investigation Publication Title"] = publications.values()
# base_info["Investigation Publication Author List"] = publications.keys() # not all authors included
# base_info["Comment[Organism]"] = organism
# base_info["Comment[Number of Cells]"] = number_of_cells
# base_info["Investigation PubMed ID"] = pubmed_url # is link for now, not just ID


# # query pubmed website for publication info
# url_pubmed = "https://pubmed.ncbi.nlm.nih.gov/"+pubmed_id
# r = requests.get(url_pubmed, allow_redirects=True).text
# soup = BeautifulSoup(r, "html.parser")
# publication_title = soup.find("title").text.split(" - Pub")[0]
# # MAGEtab: publication_authors = soup.find("meta", {"name":"citation_authors"}).get("content")[:-1] # remove trailing ;
# publication_doi = soup.find("meta", {"name":"citation_doi"}).get("content")
# publication_public_release_date = soup.find("meta", {"name":"citation_date"}).get("content")
# publication_status = None

# # compare publishing date to today to get publication_status
# date_today = time.strptime(today, "%Y-%m-%d")
# date_published = time.strptime(publication_public_release_date, "%m/%d/%Y")
# if date_today > date_published:
#     publication_status = "published"
# else:
#     publication_status = "submitted"

# # save info to dict and write output file
# base_info = {"Comment[organism]" : organism,
#               "Comment[number of cells]" : number_of_cells}
# with open(path+"base_info.tsv", "w") as f:
#     for key in base_info.keys():
#         f.write("%s\t%s\n"%(key, base_info[key]))

# ###########################
# # pull linked info from ArrayExpress
# url_ae = "https://www.ebi.ac.uk/biostudies/api/v1/studies/"+scExpressionAtlasAccession
# r = requests.get(url_ae, allow_redirects=True)
# link_valitidy = response_status(r, url_ae)
# if link_valitidy == 404:
#     print("No ArrayExpress data connected to this study.")
# # data = r.json()
# # attributes = data["attributes"]
# # parsed_attributes={}
# # # parsed_attributes contains Title, ReleaseDate
# # for elem in attributes:
# #     parsed_attributes[elem["name"]] = elem["value"]
# # section_attributes = data["section"]["attributes"]
# # for elem in section_attributes:
# #     parsed_attributes[elem["name"]] = elem["value"]
# # # url_test="https://www.ebi.ac.uk/biostudies/api/v1/studies/E-GEOD-152766"
# # # r = requests.get(url_test, allow_redirects=True)
# # # print(r)