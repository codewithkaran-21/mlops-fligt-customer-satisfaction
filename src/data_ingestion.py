import os 
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self , raw_data_path , ingested_data_dir):
        self.raw_data_path = raw_data_path
        self.ingested_data_dir = ingested_data_dir
        logger.info("Data Ingestion Started")

    def craete_ingested_data_dir(self):
        try:
            os.makedirs(self.ingested_data_dir, exist_ok=True)
            logger.info(f"Ingested data directory created at {self.ingested_data_dir}")
        except Exception as e:
            raise CustomException(f"Error creating ingested data directory: {e}")
        
    def split_data(self,train_path,test_path,test_size=0.2, random_state=42):
        try:
            data = pd.read_csv(self.raw_data_path)
            logger.info(f"Raw data loaded from {self.raw_data_path} , shape: {data.shape}")
            train_data , test_data = train_test_split(data , test_size=test_size, random_state=random_state)
            logger.info(f"Data splited into train and test sets with sizes: {train_data.shape}, {test_data.shape}")

            train_data.to_csv(train_path,index=False)
            test_data.to_csv(test_path,index=False)
            logger.info("Training and testing data saved sucesffuly")

        except Exception as e:
            raise CustomException(f"Error during data splitting: {str(e)}",sys)
        
if __name__ == "__main__":
    try:
        ingestion = DataIngestion(raw_data_path=RAW_DATA_PATH,ingested_data_dir=INGESTED_DATA_DIR)
        ingestion.craete_ingested_data_dir()
        ingestion.split_data(train_path = TRAIN_DATA_PATH,test_path=TEST_DATA_PATH)

    except CustomException as ce:
        logger.error(str(ce))