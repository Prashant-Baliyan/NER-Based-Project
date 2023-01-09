import argparse
import os
from src.NER_utils import *
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataPreprocessingConfig, \
    ModelTrainConfig, PredictPipelineConfig
from transformers import AutoTokenizer, AutoConfig
from from_root import from_root
from src.constants import *
import logging

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class Configuration:
    def __init__(self):
            logging.info("Reading Config file")
            self.config = read_config(file_name=CONFIG_FILE_NAME)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
            dataset_name = self.config[DATA_INGESTION_KEY][DATASET_NAME]
            subset_name = self.config[DATA_INGESTION_KEY][SUBSET_NAME]

            data_store = os.path.join(self.config[PATH_KEY][ARTIFACTS_KEY],
                                      self.config[PATH_KEY][DATA_STORE_KEY])

            data_ingestion_config = DataIngestionConfig(
                dataset_name=dataset_name,
                subset_name=subset_name,
                data_path=data_store
            )
            return data_ingestion_config

def main():
    Configuration = Configuration()
    Configuration.get_data_ingestion_config()

if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> data_ingestion_config entity extraction started <<<<<")
        main()
        logging.info(f">>>>> data_ingestion_config entity extraction completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e