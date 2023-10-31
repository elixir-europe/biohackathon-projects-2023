#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 11:48:20 2023

@author: hannah
"""

import requests
import logging
import zipfile
from csv import reader, DictWriter, writer
import shutil
import os
from bs4 import BeautifulSoup

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

def get_experiment(path, scExpressionAtlasAccession, experiment_design=False, experiment_metadata=False):    
    # download experiment metadata
    if experiment_metadata == True:
        url="https://www.ebi.ac.uk/gxa/sc/experiment/"+scExpressionAtlasAccession+"/download/zip?fileType=experiment-metadata&accessKey="
        r = requests.get(url, allow_redirects=True)
        response_stat = response_status(r, url, get_experiment.__name__)
        if response_stat >= 200 and response_stat < 300:
            open(path+"experimental_metadata.zip","wb").write(r.content)
            with zipfile.ZipFile(path+"experimental_metadata.zip", "r") as zip_ref:
                zip_ref.extractall(temp)
            shutil.rmtree(temp)
            print("[INFO] download of experimental metadata zip archive done")
        else:
            print("[WARNING] no experiment metadata information could be downloaded")

def make_paths(input_scEA):
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
        
    return path, temp, log, input_scEA

def get_basics():
    # download basic info: title, publication, organism, number of cells, pubmed link
    url = "http://ftp.ebi.ac.uk/pub/databases/microarray/data/atlas/sc_experiments/"
    r = requests.get(url, allow_redirects=True)
    response_stat = response_status(r, url, get_basics.__name__)
    if response_stat >= 200 and response_stat < 300:
        r_text = r.text
        soup = BeautifulSoup(r_text, "html.parser")
        anchor_tags = soup.find_all("a")
        directory_names = []
        for tag in anchor_tags:
            href = tag.get("href")
            if href.endswith("/"):
                directory_name = href[:-1]
                directory_names.append(directory_name)
        return directory_names[1:-1]
        print("[INFO] download of basic information done")
    else:
        print("[WARNING] no basic information could be downloaded")


# main run
scEA_investigations = get_basics()

# scEA_investigations = ["E-MTAB-11006"]#, "E-GEOD-152766"]#, "E-CURD-83", "E-GEOD-141730", "E-ENAD-50", "E-ENAD-49", "E-GEOD-158761", 
                        # "E-GEOD-161332", "E-GEOD-123013", "E-GEOD-121619", "E-CURD-5", "E-CURD-4", "E-ENAD-30"]

# scEA_investigations = "E-MTAB-11006"
for accession in scEA_investigations:
    path, temp, log, user_input_scEA = make_paths(input_scEA=accession)
    get_experiment(path, user_input_scEA, experiment_metadata=True)
