from src.Text_Summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Text_Summarizer import logger
from src.Text_Summarizer.pipeline.stage_02_data_validation import DataValidationPipeline
STAGE_NAME = 'Data Ingestion Stage'

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed  <<<<<<<")
except Exception as e:
    raise e

STAGE_NAME = 'Data Validation Stage'

try: 
    logger.info(f">>>>>> stage {STAGE_NAME} started  <<<<<<<")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed  <<<<<<<")
except Exception as e:
    raise e


