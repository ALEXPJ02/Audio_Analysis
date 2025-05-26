# config_loader.py
import yaml

def load_config(config_path="config/default.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)