from src.Text_Summarizer.constants import * # constanst icerisinde degiskenleri import ettik
from src.Text_Summarizer.utils.common import read_yaml, create_directories # common.py icerisinde read_yaml ve create_directories methodlarini import ettik
from src.Text_Summarizer.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig: # Yukarida DataIngestionConfig sinifi icerisinde tanimlamis oldugum degiskenleri return edecektir
        config = self.config.data_ingestion # root_dir, local_data_file, source_URL, unzip_dir keylerine erisim sagliyorum

        create_directories([config.root_dir]) # artifacts/data_ingestion isimli bir klasor olustuyorum

        data_ingestion_config = DataIngestionConfig( # Ust hucrede tanimlamis oldugum sinifin nesnesini yaratiyorum
            root_dir=config.root_dir, #artifacts/data_ingestion
            source_URL=config.source_URL, #https://github.com/entbappy/Branching-tutorial/raw/master/summarizer-data.zip
            local_data_file=config.local_data_file, # artifacts/data_ingestion/data.zip
            unzip_dir=config.unzip_dir, # artifacts/data_ingestion
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILE= config.ALL_REQUIRED_FILE
        )
        return data_validation_config
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path= config.data_path,
            tokenizer_name= config.tokenizer_namr
        )
        return data_transformation_config