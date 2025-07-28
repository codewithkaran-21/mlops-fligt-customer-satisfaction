import pandas as pd 
from sklearn.preprocessing import StandardScaler
from config.paths_config import *
from src.logger import get_logger
from src.custom_exception import CustomException
import sys 

logger = get_logger(__name__)


class DataPreprocessing:

    def __init__(self):
        self.train_path = TRAIN_DATA_PATH
        self.preprocessed_data_path = PROCESSED_DATA_PATH

    def load_data(self):
        try:
            logger.info(f"Data Preprocessing Started :")
            df = pd.read_csv(self.train_path)
            logger.info(f"Data loaded scuccessfully from {self.train_path}, shape: {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise CustomException(f"Error loading data: {str(e)}", sys)
    def drop_unnecessary(self,df,columns):
        try:
            logger.info(f"Data Unnecessary columns Started  : {columns}")
            df = df.drop(columns = columns , axis=1)
            logger.info(f"Successfully droped columns -> : {columns}")
            return df 
        except Exception as e:
            logger.error(f"Error while dropping columns ")
            raise CustomException(f"Error while dropping columns: {str(e)}", sys)
    
    def handle_outliers(self , df , columns):
        try:
            logger.info(f" Handling Outlier for columns : {columns}")
            for column in columns:
                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)
                IQR = Q3 - Q1

                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                df[column] = df[column].clip(lower = lower_bound , upper = upper_bound)
            logger.info(f"Outliers handled for column: {column}")
            return df
        except Exception as e:
            logger.error(f"Error while handling outliers: {str(e)}")
            raise CustomException(f"Error while handling outliers: {str(e)}", sys)
    
    def handle_null_values(self,df,columns):
        try:
            logger.info(f"Handling null values for columns: {columns}")
            df[columns] = df[columns].fillna(df[columns].median())
            logger.info(f"Null values handled for columns: {columns}")
            return df
        except Exception as e:
            logger.error(f"Error while handling null values: {str(e)}")
            raise CustomException(f"Error while handling null values: {str(e)}", sys)
    
        
    def save_data(self,df):
        try:
            # os.makedirs(PROCESSED_DIR, exist_ok=True)
            os.makedirs(os.path.dirname(self.preprocessed_data_path), exist_ok=True)
            df.to_csv(self.preprocessed_data_path, index=False)
            logger.info(f"Preprocessed data saved sucessfullu to {self.preprocessed_data_path}")
        except Exception as e :
            logger.error("Error while saving data")
            raise CustomException(f"Error while saving data: {str(e)}", sys)
        
    def run(self):
        try:
            logger.info("Data Preprocessing Pipeline Started")
            df = self.load_data()
            df = self.drop_unnecessary(df, columns=["MyUnknownColumn","id"])
            column_to_handle_outliers = ['Flight Distance','Departure Delay in Minutes','Arrival Delay in Minutes', 'Checkin service']  # Replace with actual column names
            df = self.handle_outliers(df, column_to_handle_outliers)
            df = self.handle_null_values(df , 'Arrival Delay in Minutes')

            self.save_data(df)
            logger.info("Data Preprocessing Pipeline Completed Successfully")
        except Exception as ce:
            logger.error(f"Error in Data Preprocessing Pipeline: {str(ce)}")
        
if __name__ == "__main__":
    preprocessor = DataPreprocessing()
    preprocessor.run()