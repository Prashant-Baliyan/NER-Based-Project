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

    def get_data_validation_config(self) -> DataValidationConfig:

            # Load data from the disk location artifacts store
            # os.path.join(from_root(),-- path to the data_store)

            split = self.config[DATA_VALIDATION_KEY][DATA_SPLIT]
            columns = self.config[DATA_VALIDATION_KEY][COLUMNS_CHECK]

            null_value_check = self.config[DATA_VALIDATION_KEY][TYPE_CHECK]
            type_check = self.config[DATA_VALIDATION_KEY][NULL_CHECK]

            data_validation_config = DataValidationConfig(
                dataset=None,
                data_split=split,
                columns_check=columns,
                type_check=type_check,
                null_check=null_value_check
            )

            return data_validation_config
            
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
            model_name = self.config[BASE_MODEL_CONFIG][BASE_MODEL_NAME]
            tags = self.config[DATA_PREPROCESSING_KEY][NER_TAGS_KEY]

            index2tag = {idx: tag for idx, tag in enumerate(tags)}
            tag2index = {idx: tag for idx, tag in enumerate(tags)}

            tokenizer = AutoTokenizer.from_pretrained(self.config[BASE_MODEL_CONFIG][BASE_MODEL_NAME])

            data_preprocessing_config = DataPreprocessingConfig(
                model_name=model_name,
                tags=tags,
                index2tag=index2tag,
                tag2index=tag2index,
                tokenizer=tokenizer
            )
            return data_preprocessing_config
def main():
    Configuration = Configuration()
    Configuration.data_validation_config()

if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> data_ingestion_config entity extraction started <<<<<")
        main()
        logging.info(f">>>>> data_ingestion_config entity extraction completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e