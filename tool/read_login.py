import yaml

def read_yaml():
    with open("../data/login.yaml","r",encoding="utf-8") as f:
        return yaml.load(f)





