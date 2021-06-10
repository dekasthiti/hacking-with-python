from argparse import ArgumentParser
import json
import os
import yaml
import glob

def load_yaml(dir):
    yaml_files = glob.iglob(f"{dir}/*.yaml", recursive = True)
    for yaml_file in yaml_files:
        path = os.path.dirname(yaml_file)
        filename = os.path.basename(yaml_file).split('.')[0]
        with open(yaml_file, "r") as fp:
            yaml_obj = yaml.load(fp, Loader = yaml.FullLoader)
            print(yaml_obj)
            yaml_to_json(yaml_obj, filename, path, )
            
def yaml_to_json(yaml_obj, filename, path):
    with open(f"{path}/{filename}.json", "w") as json_fp:
        json.dump(yaml_obj, json_fp, indent = '\t')
        
        
def get_output():
    return os.path.join(os.curdir, "config_output.json")
    
    
if __name__ == '__main__':
    parser = ArgumentParser()
    
    parser.add_argument('--dir', default = None)
    args = parser.parse_args()
    
    load_yaml(args.dir)
    