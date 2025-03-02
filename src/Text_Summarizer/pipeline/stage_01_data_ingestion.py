from src.Text_Summarizer.config.configration import ConfigurationManager
from src.Text_Summarizer.components.data_ingestion import DataIngestion
from src.Text_Summarizer import logger

STAGE_NAME = "Data Ingestion stage"  # Aşama ismi

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Konfigürasyon yöneticisini oluştur
        config = ConfigurationManager()
        # Veri alım konfigürasyonunu al
        data_ingestion_config = config.get_data_ingestion_config()
        # DataIngestion sınıfını başlat
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # Dosyayı indir
        data_ingestion.download_file()
        # Zip dosyasını çıkar
        data_ingestion.extract_zip_file()
