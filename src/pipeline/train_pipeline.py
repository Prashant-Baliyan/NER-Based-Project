from src.config.configuration import Configuration
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_preparation import DataPreprocessing
# from src.components.model_training import TrainTokenClassifier
from typing import Any, Dict, List, ClassVar
import logging
import os

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class TrainPipeline:
    def __init__(self, config):
        self.config = config

    def run_data_ingestion(self) -> Dict:
            logging.info(" Running Data Ingestion pipeline ")
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            data = data_ingestion.get_data()
            return data
    
    def run_data_validation(self, data) -> List[List[bool]]:
            logging.info(" Running Data validation Pipeline ")
            validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                        data=data)
            checks = validation.drive_checks()
            return checks

    def run_data_preparation(self, data) -> Dict:
            logging.info(" Running Data Preparation pipeline ")
            data_preprocessng = DataPreprocessing(data_preprocessing_config=self.config.get_data_preprocessing_config(),
                                                  data=data)
            data = data_preprocessng.prepare_data_for_fine_tuning()
            return data

    def run_pipeline(self):
        data = self.run_data_ingestion()
        checks = self.run_data_validation(data=data)
        if sum(checks[0]) == 3:
            logging.info("Checks Completed")
            processed_data = self.run_data_preparation(data=data)
            logging.info(f"Preprocessed Data {processed_data}")
            #self.run_model_training(data=processed_data)
        else:
            logging.error("Checks Failed")    

if __name__ == "__main__":
    pipeline = TrainPipeline(Configuration())
    pipeline.run_pipeline()