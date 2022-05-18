import os.path
import yaml


def parse_yaml(file_name):
    params = {}
    base_path = os.path.dirname(os.path.dirname(__file__))
    yaml_path = os.path.join(base_path, "config", file_name)
    with open(yaml_path, "r", encoding="utf-8") as file:
        params = yaml.load(file.read(), Loader=yaml.SafeLoader)
    return params

