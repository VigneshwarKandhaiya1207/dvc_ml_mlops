import os
import sys
import pandas as pd
from utils.main_utils import read_yaml,create_directory
import argparse



def get_data(config_path:str):
    config=read_yaml(config_path)

    remote_data_path=config['data_source']
    df = pd.read_csv(remote_data_path,sep=';')

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path= os.path.join(artifacts_dir,raw_local_dir)
    raw_local_file_path=os.path.join(raw_local_dir_path,raw_local_file)

    #Creating Drirectories.

    create_directory(dirs=[raw_local_dir_path])

    # Pushing the file to data.csv

    df.to_csv(raw_local_file_path,sep=',',index=False)

if __name__== "__main__":
    print("<<<<<< Running Stage 01 >>>>>>")
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_args=args.parse_args()

    get_data(config_path=parsed_args.config)

