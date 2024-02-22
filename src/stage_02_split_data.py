import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils.main_utils import read_yaml,create_directory,save_data_df


def split_and_save_data(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    artifacts_dir=config['artifacts']['artifacts_dir']
    raw_local_dir=config['artifacts']['raw_local_dir']
    raw_local_file=config['artifacts']['raw_local_file']

    raw_local_file_path=os.path.join(artifacts_dir,raw_local_dir,raw_local_file)
    df=pd.read_csv(raw_local_file_path)

    split_ratio=params['base']['split_ratio']
    random_state=params['base']['random_state']

    train,test = train_test_split(df,test_size=split_ratio,random_state=random_state)

    split_data_dir=config['artifacts']['split_data_dir']
    train_data_file_name=config['artifacts']['train']
    test_data_file_name=config['artifacts']['test']

    create_directory([os.path.join(artifacts_dir,split_data_dir)])

    train_data_file_path=os.path.join(artifacts_dir,split_data_dir,train_data_file_name)
    test_data_file_path=os.path.join(artifacts_dir,split_data_dir,test_data_file_name)

    for data,data_path in (train,train_data_file_path),(test,test_data_file_path):
        save_data_df(data,data_path)

if __name__=="__main__":
    print("<<<<<< Running Stage 02 >>>>>>")
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args=args.parse_args()

    split_and_save_data(config_path=parsed_args.config,params_path=parsed_args.params)


