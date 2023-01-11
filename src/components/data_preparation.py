from src.entity.config_entity import DataPreprocessingConfig
from src.config.configuration import Configuration
from typing import Any, Dict
import logging
import os

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )

class DataPreprocessing:
    def __init__(self, data_preprocessing_config: DataPreprocessingConfig, data: Any):
        self.data_preprocessing_config = data_preprocessing_config
        self.data = data

    def create_tag_names(self, batch):
        return {"ner_tags_str": [self.data_preprocessing_config.index2tag[idx] for idx in batch["ner_tags"]]}

    def tokenize_and_align_labels(self, data):
            logging.info(" Tokenize and align labels ")
            tokenizer = self.data_preprocessing_config.tokenizer

            tokenized_inputs = tokenizer(data["tokens"], truncation=True,
                                         is_split_into_words=True)
            labels = []

            for idx, label in enumerate(data["ner_tags"]):
                word_ids = tokenized_inputs.word_ids(batch_index=idx)
                previous_word_idx = None
                label_ids = []
                for word_idx in word_ids:
                    if word_idx is None or word_idx == previous_word_idx:
                        label_ids.append(-100)
                    else:
                        label_ids.append(label[word_idx])
                    previous_word_idx = word_idx
                labels.append(label_ids)

            tokenized_inputs["labels"] = labels

            return tokenized_inputs

    def encode_en_dataset(self, corpus):
            return corpus.map(self.tokenize_and_align_labels,
                              batched=True,
                              remove_columns=['langs', 'ner_tags', 'tokens'])

    def prepare_data_for_fine_tuning(self) -> Dict:
            # Map Data with create_tag_names
            self.data = self.data.map(self.create_tag_names)

            # Map word-id and label id into main data
            panx_en_encoded = self.encode_en_dataset(self.data)

            return panx_en_encoded

def main():
    project_config = Configuration()
    preprocessing = DataPreprocessing(project_config.get_data_preprocessing_config())
    prepare_data_for_fine_tuning = preprocessing.prepare_data_for_fine_tuning()
    print(prepare_data_for_fine_tuning)


if __name__ == "__main__":
    try:
        logging.info("\n********************")
        logging.info(f">>>>> data_ingestion_config entity extraction started <<<<<")
        main()
        logging.info(f">>>>> data_ingestion_config entity extraction completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e