import pandas as pd
from src.config.configuration import Configuration
from src.entity.config_entity import DataValidationConfig
from src.components.data_ingestion import DataIngestion
from typing import Dict, List
import logging
import os

STAGE = "Data Validation stage" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class DataValidation:
    def __init__(self, data_validation_config: DataValidationConfig, data: Dict):
        logging.info(" Data Validation Started ")
        self.data_validation_config = data_validation_config
        self.data = data

    def check_columns_names(self) -> bool:
            logging.info(" Checking Columns of all the splits ")
            column_check_result = list()

            for split_name in self.data_validation_config.data_split:
                column_check_result.append(
                    sum(pd.DataFrame(self.data[split_name]).columns == self.data_validation_config.columns_check)
                )

            logging.info(f" Check Results {column_check_result}")

            if sum(column_check_result) == len(self.data_validation_config.data_split) * \
                    len(self.data_validation_config.columns_check):
                return True
            else:
                return False

    def type_check(self) -> bool:

            """ Implement Type Check Here """
            logging.info(" Checking type check of all the splits ")
            result = self.data_validation_config.type_check
            return True


    def null_check(self) -> bool:
  
            """ Implement null Check Here """
            logging.info(" Checking null check of all the splits ")
            result = self.data_validation_config.null_check
            return True

    def drive_checks(self) -> List[List[bool]]:
        logging.info(" Checks Initiated  ")
        checks = list()
        checks.append(
            [
                self.check_columns_names(),
                self.type_check(),
                self.null_check()
            ]
        )
        logging.info(f" Checks Completed Result : {checks}")
        return checks

def main():
    project_config = Configuration()
    ingestion = DataIngestion(project_config.get_data_ingestion_config())
    en_data = ingestion.get_data()

    validate = DataValidation(data_validation_config=project_config.get_data_validation_config()
                              , data=en_data)
    check = validate.drive_checks()
    print(check)

if __name__ == "__main__":
    try:
        logging.info("\n********************")
        logging.info(f">>>>> data_ingestion_config entity extraction started <<<<<")
        main()
        logging.info(f">>>>> data_ingestion_config entity extraction completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e