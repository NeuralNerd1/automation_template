import yaml

def load_elements(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)
