#!/usr/bin/env python3

from argparse import RawTextHelpFormatter
import requests
import argparse
import json
import re
import os
from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError
from typing import Union

# -- #
# Hardcoded values
# -- #
biosamples_endpoints = {
    "prod": "https://www.ebi.ac.uk/biosamples/samples/",
    "dev": "https://wwwdev.ebi.ac.uk/biosamples/samples/"
}
input_json_schema_filepath = "./input-schema.json"

# -- #
# Code blocks
# -- #
def load_json_file(file):
    """ 
    Function to load a JSON file as a dictionary.
    Args:
        file (str): Path to the file to be loaded.
    """
    if not os.path.exists(file):
        raise FileNotFoundError(f"The file '{file}' does not exist.")
    if not os.path.isfile(file):
        raise ValueError(f"The path '{file}' is not a file.")
    if not file.endswith('.json'):
        raise ValueError(f"The given file '{file}' is not a JSON file based on its extension.")

    try:
        with open(file, "r") as f:
            loaded_dict = json.load(f)
        return loaded_dict
    except json.JSONDecodeError:
        raise ValueError(f"The file content of the given file '{file}' is not valid JSON.")

def handle_input_dict(input):
    """ 
    Function to handle the input: assert that it's either a dictionary or
        the filepath to an existing file containing the dictionary
        
    Args:
        input (dict or str): Dictionary or filepath to the dictionary JSON.
    """
    if isinstance(input, dict):
        return input
    else:
        try:
            loaded_dict = load_json_file(input)
            
            if not isinstance(loaded_dict, dict):
                raise ValueError(f"The file '{input}' does not contain a valid dictionary.")
            
            return loaded_dict

        except json.JSONDecodeError:
            raise ValueError(f"The file '{input}' is not a valid JSON file.")


def get_webin_auth_token(
        credentials_dict,
        header={"Content-Type": "application/json"},
        auth_url="https://wwwdev.ebi.ac.uk/ena/submit/webin/auth/token"
    ):
    """
    Obtain Webin authentication token.

    Args:
    credentials_dict (dict): The password dictionary for authentication.
    header (dict): The header information.
    auth_url (str): The URL for authentication.

    Returns:
    str: The obtained token.
    """
    data = json.dumps({
        "authRealms": ["ENA"],
        "password": credentials_dict["password"],
        "username": credentials_dict["username"]
    })
    try:
        response = requests.post(auth_url, headers=header, data=data)
        token = response.content.decode('utf-8')
    except Exception as e:
        raise e
    
    if response.status_code != 200:
        response_content = response.content.decode('utf-8')
        error_message = f"ERROR when generating token. See response's content below:\n{response_content}"
        raise ValueError(error_message)
    
    return token

def get_header(token):
    """
    Obtain the header using a token.

    Args:
    token (str): The Webin auth token.

    Returns:
    dict: The header.
    """
    return {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/hal+json",
        "Authorization": f"Bearer {token}"
    }

def validate_bs_accession(accession_str):
    """
    Validates that the given accession string conforms to the specified regex format.
        See: https://registry.identifiers.org/registry/biosample
    
    Args:
    accession_str (str): The accession string to be validated.
    """
    
    pattern = r'^SAM[NED](\w)?\d+$'
    
    if not re.match(pattern, accession_str):
        raise ValueError(f"The provided accession string '{accession_str}' does not match the required format.")

def validate_json_against_schema(json_doc: Union[dict, str], json_schema: Union[dict, str]):
    """
    Validates a JSON document against a given JSON Schema.

    Args:
    json_filepath (dict, str): JSON document or the filepath to it.
    schema_filepath (dict, str): JSON schema or the filepath to it.
    """
    # Load both files if needed
    if isinstance(json_doc, dict):
        json_data = json_doc
    else:
        json_data = load_json_file(json_doc)
        
    if isinstance(json_schema, dict):
        schema_data = json_schema
    else:
        schema_data = load_json_file(json_schema)

    # Validating JSON against the schema
    try:
        validate(instance=json_data, schema=schema_data)
        return True
    except ValidationError as e:
        raise ValidationError(
            f"Found an error when validating the JSON document with its JSON Schema. This may mean that the given input is invalid."
            f"JSON validation error: {e.message}"
        )
    except SchemaError as e:
        raise SchemaError(f"Schema error: {e.message}")
    
    return False

class BiosamplesRecord:
    """
    Class representing a record for biosamples to be extended.

    Attributes:
    biosamples_externalReferences: dict or filepath to external references
    production: boolean indicating environment mode
    """

    def __init__(self, bs_accession):
        """
        Initialize the BiosamplesRecord with provided arguments.

        Args:
        bs_accession: a valid Biosamples accession (e.g. SAMEA112654119)
        """
        validate_bs_accession(bs_accession)
        self.bs_accession = bs_accession

    def display(self):
        """
        Display the attributes for demonstration purposes.
        """
        print("Biosamples Credentials:", self.biosamples_credentials)
        print("Biosamples External References:", self.biosamples_externalReferences)
        print("Production Mode:", self.production)

    def fetch_bs_json(self, biosamples_endpoint):
        """
        Fetches the BioSample's record (JSON) of the accession.

        Args:
            biosamples_endpoint (str): The endpoint to be used to fetch the record's JSON.
        """
        
        self.biosamples_url = f"{biosamples_endpoint}{self.bs_accession}.json"
        
        try:
            r = requests.get(self.biosamples_url)  # No auth token needed, it's public info
            
            if r.status_code != 200:
                raise RuntimeError(f"Expected status code 200, but received {r.status_code}. Used URL: '{self.biosamples_url}'. Response content: {r.text}")
            
            # Attempt to load the JSON content
            response_json = r.json()                
            if not isinstance(response_json, dict):
                raise ValueError(f"The response content is not a valid dictionary. Content: {r.text}")
            
        except requests.RequestException as e:
            raise RuntimeError(f"Error making the request. Details: {e}")
        
        except json.JSONDecodeError:
            raise ValueError(f"The server response is not valid JSON. Content: {r.text}")
        
        self.bs_json = response_json
        return self.bs_json
    
    def load_bs_json(self, bs_json_file: str = None, bs_json: dict = None):
        """
        Loads a given JSON, or the file containing it, as the BioSample's record (JSON) for this instance.
            It is an alternative to fetching it directly from BioSample.

        Args:
            bs_json_file (str): The file containing the Biosamples JSON metadata of the accession
            bs_json (dict): The already loaded Biosamples JSON metadata of the accession
        """
        if bs_json:
            if isinstance(bs_json, dict): 
                self.bs_json = bs_json
                return self.bs_json
            else:
                raise TypeError(f"Given 'bs_json' is of type '{type(bs_json)}' instead of type 'dict'.")
        elif bs_json_file:
            bs_json = load_json_file(bs_json_file)
            self.bs_json = bs_json
            return self.bs_json
        else:
            raise ValueError(f"Neither the file containing the Biosamples JSON nor the Biosamples JSON itself were given to load it into the instance.")

    def pop_links(self):
        """
        Removes "_links" array (which is added automatically after updating the biosamples on the BioSample's side).
        """
        
        if "_links" not in self.bs_json:
            return self.bs_json
        
        self.bs_json.pop("_links")
        return self.bs_json

    def extend_externalReferences(self, new_ext_refs_list):
        """ Extends the JSON of the BioSample's record with new externalReferences
        """
        if not self.bs_json:
            self.fetch_bs_json()
        self.pop_links()

        if "externalReferences" not in self.bs_json:
            ext_refs_list = new_ext_refs_list
        else:
            existing_ext_refs_list = self.bs_json["externalReferences"]

            # Convert dictionaries to JSON strings and add them to a set for deduplication
            unique_refs_set = set(json.dumps(dic) for dic in existing_ext_refs_list + new_ext_refs_list)

            # Convert JSON strings back to dictionaries
            ext_refs_list = [json.loads(dic_str) for dic_str in unique_refs_set]
        
        self.bs_json["externalReferences"] = ext_refs_list
        return self.bs_json
    
    def update_remote_record(self, header, webin_auth="?authProvider=WEBIN"):
        """
        Updates the remote record of the BioSample's accession with the current sample JSON.

        Args:
            header (dict): The HTTP headers to use in the request.
            webin_auth (str, optional): The authentication provider for WEBIN.
        """
        update_url = f"{self.biosamples_url}{webin_auth}"
        updated_json = json.dumps(self.bs_json)

        try:
            r = requests.put(update_url, headers=header, data=updated_json)
            
            # Check if HTTP status code indicates success (2xx range)
            if r.status_code != 200:
                raise RuntimeError(f"Expected status code 200, but received {r.status_code}. Response content: {r.text}")
        
        except requests.RequestException as e:
            raise RuntimeError(f"Error making the request. Details: {e}")
        
        return r.text
        

def main(biosamples_credentials, biosamples_externalReferences, production):
    """
    Main function to be executed when script is run.

    Args:
    biosamples_credentials: Dictionary with the credentials of the submitter of the existing Biosamples records.
    biosamples_externalReferences: Dictionary containing the mapping between the 
    production: Boolean indicating the environment of BioSamples to use.
    """
    validate_json_against_schema(json_doc=biosamples_externalReferences, json_schema=input_json_schema_filepath)
    token = get_webin_auth_token(biosamples_credentials)
    header = get_header(token)

    if production:
        biosamples_endpoint = biosamples_endpoints["prod"]
    else:
        biosamples_endpoint = biosamples_endpoints["dev"]

    for biosample_r in biosamples_externalReferences["biosampleExternalReferences"]:
        bs_accession = biosample_r["biosampleAccession"]
        BSrecord = BiosamplesRecord(bs_accession)
        BSrecord.fetch_bs_json(biosamples_endpoint)
        # To test it without the fetching, you can download it manually and then use:
        #   BSrecord.load_bs_json(bs_json_file="downloaded-json.json")
        new_ext_refs_list = biosample_r["externalReferences"]
        BSrecord.extend_externalReferences(new_ext_refs_list)
        BSrecord.update_remote_record(header)
        
if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Handle biosamples records.")
    description = "This script extends a set of existing Biosamples records with a list of provided external references."
    parser = argparse.ArgumentParser(prog="biosamples-externalReferences.py",
                                    description=description,
                                    formatter_class=RawTextHelpFormatter)
    parser.add_argument("biosamples_credentials", help="Either a dictionary or filepath to the BioSamples credentials.")
    parser.add_argument("biosamples_externalReferences", help="Either a dictionary or filepath to the BioSamples' accessions mapping with external references.")
    parser.add_argument("--production", action="store_true", help="Boolean indicating the usage of the production environment of BioSamples. If not present, the development instance will be used.")
    # Handle inputs
    parsed_args = parser.parse_args()
    biosamples_credentials = handle_input_dict(parsed_args.biosamples_credentials)
    biosamples_externalReferences = handle_input_dict(parsed_args.biosamples_externalReferences)

    main(biosamples_credentials, biosamples_externalReferences, parsed_args.production)