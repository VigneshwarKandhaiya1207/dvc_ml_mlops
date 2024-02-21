import argparse
from src.utils.main_utils import read_yaml

def get_data(config_path:str):
    config=read_yaml(config_path)
    for i in range(len(config['changes'])):
        data_path=config['changes'][i]
        for key,value in data_path.items():
            if value is True:
                print(key, value)


if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    parsed_data=args.parse_args()
    get_data(parsed_data.config)