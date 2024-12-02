import sys
print(sys.path)
sys.path.append(r"E:\dlprojects\text-summarizer-project")
from src.textsummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textsummarization import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e