import argparse
import os
import pandas as pd
from src.utils.main_utils import read_yaml,create_directory
from sklearn.linear_model import ElasticNet
import joblib



def train_data(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)

    artifacts_dir=config['artifacts']['artifacts_dir']
    split_data_dir=config['artifacts']['split_data_dir']
    train_data_filename=config['artifacts']['train']

    train_data_file_path=os.path.join(artifacts_dir,split_data_dir,train_data_filename)

    alpha=params['model_params']['ElasticNet']['alpha']
    l1_ratio=params['model_params']['ElasticNet']['l1_ratio']
    random_state=params['base']['random_state']

    model_dir=config['artifacts']['model_dir']
    model_file=config['artifacts']['model_file']

    model_dir_path=os.path.join(artifacts_dir,model_dir)

    model_file_name=os.path.join(model_dir_path,model_file)

    create_directory([model_dir_path])
    
    df=pd.read_csv(train_data_file_path)

    train_x = df.drop('quality',axis=1)
    train_y=df['quality']

    lr=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)

    lr.fit(train_x,train_y)

    joblib.dump(lr,model_file_name)

    print("coeff: {0}, intercept: {1}".format(lr.coef_,lr.intercept_))

    print("score = {}".format(lr.score(train_x,train_y)))

    print("done")






if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")

    parsed_args=args.parse_args()

    train_data(config_path=parsed_args.config,params_path=parsed_args.params)