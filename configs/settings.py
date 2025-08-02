import os.path

import yaml
from dotenv import load_dotenv

def load_configs(path="config/configs.yml"):
    load_dotenv()
    with open(path, "r") as f:
        raw = f.read()
    resolved = os.path.expandvars(raw)
    return yaml.safe_load(resolved)
