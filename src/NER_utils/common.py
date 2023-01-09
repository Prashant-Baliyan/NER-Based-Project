import os
import yaml
import logging
from from_root import from_root
from typing import Dict
import json

def read_config(file_name: str) -> Dict:
    """
    This Function reads the config.yaml from root directory and
    return configuration in dictionary.

    Returns: Dict of config
    """
    config_path = os.path.join(from_root(), file_name)
    with open(config_path) as config_file:
        content = yaml.safe_load(config_file)

    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")