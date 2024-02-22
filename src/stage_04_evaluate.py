import os
import numpy as np
import joblib
import pandas as pd
import argparse
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from src.utils.main_utils import read_yaml,create_directory,save_reports
import json

def evaluate_metrics(actual_values,predicted_values):
    mae=mean_absolute_error(actual_values,predicted_values)
    rmse=np.sqrt(mean_squared_error(actual_values,predicted_values))
    r2=r2_score(actual_values,predicted_values)

    return (mae,rmse,r2)

def evaluate(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    artifacts_dir=config['artifacts']['artifacts_dir']
    split_data_dir=config["artifacts"]['split_data_dir']
    test_data_filename=config['artifacts']['test']
    score_dir=config['artifacts']['scores_dir']
    score_file_name=config['artifacts']["scores_file"]

    test_data_file_path=os.path.join(artifacts_dir,split_data_dir,test_data_filename)

    model_dir=config['artifacts']['model_dir']
    model_filename=config['artifacts']["model_file"]

    df=pd.read_csv(test_data_file_path)

    test_x=df.drop('quality',axis=1)
    test_y=df['quality']

    model_file_path=os.path.join(artifacts_dir,model_dir,model_filename)

    lr=joblib.load(model_file_path)

    predicted_values=lr.predict(test_x)

    mae,rmse,r2=evaluate_metrics(test_y,predicted_values)

    create_directory([os.path.join(artifacts_dir,score_dir)])

    scores_file_path=os.path.join(artifacts_dir,score_dir,score_file_name)
    
    scores={
        'mae':mae,
        'rmse':rmse,
        'r2':r2
    }

    save_reports(scores,scores_file_path)


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args=args.parse_args()

    evaluate(config_path=parsed_args.config,params_path=parsed_args.params)