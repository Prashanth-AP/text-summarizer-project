# from src.textsummarization.config.configuration import ConfigurationManager
from src.textsummarization.config.configuration import ConfigurationManager
from src.textsummarization.components.data_validation import DataValiadtion
# from src.textsummarization import logger


class DatavalidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_ingestion_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.download_file()
        data_validation.extract_zip_file()
