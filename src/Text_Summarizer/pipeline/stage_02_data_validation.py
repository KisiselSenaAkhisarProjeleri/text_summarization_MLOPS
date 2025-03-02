from src.Text_Summarizer.config.configration import ConfigurationManager
from src.Text_Summarizer.components.data_validation import DataValidation
from src.Text_Summarizer import logger

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_file_exists()
        