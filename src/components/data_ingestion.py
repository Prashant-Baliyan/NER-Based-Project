import argparse
import os
import logging
from datasets import load_dataset
from src.entity.config_entity import DataIngestionConfig
from src.config.configuration import Configuration

STAGE = "Data Ingestion stage" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        logging.info(" Data Ingestion Log Started ")
        self.data_ingestion_config = data_ingestion_config

    def get_data(self):
            """
            This is class is responsible for data collection from official hugging face library.
            Cross-lingual Transfer Evaluation of Multilingual Encoders 
            (XTREME) benchmark called WikiANN or PAN-X.
            
            Returns: Dict of train test validation data 
            """
            logging.info(f"Loading Data from Hugging face ")
            pan_en_data = load_dataset(self.data_ingestion_config.dataset_name,
                                       name=self.data_ingestion_config.subset_name)
            logging.info(f"Dataset Info : {pan_en_data}")

            return pan_en_data

def main():
    project_config = Configuration()
    ingestion = DataIngestion(project_config.get_data_ingestion_config())
    print(ingestion)

if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e