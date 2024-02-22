import yaml
import os
import sys

def read_yaml(filename: str)->dict:
    with open(filename,"rb") as yaml_file:
        content=yaml.safe_load(yaml_file)
    
    return content

def create_directory(dirs:list):
    for directories in dirs:
        try:
            os.makedirs(directories,exist_ok=True)
            print("The directory has got created at {0}".format(directories))
        except Exception as e:
            print(e)

def save_data_df(data,data_path):
    try:
        data.to_csv(data_path)
    except Exception as e:
        print(e)