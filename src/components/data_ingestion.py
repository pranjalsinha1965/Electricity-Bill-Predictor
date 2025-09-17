import os 
import sys 
from dataclasses import dataclass 

import pandas as pd 
from sklearn.model_selection import train_test_split 

from src.exception import FileOperatorError
from src.logger import logging 

ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts")

@dataclass 
class DataIngestionConfig: 
    # Define the default file path for raw, training and testing values 
    raw_data_file_path: str = os.path.join(ARTIFACTS_DIR, "raw_data.csv")
    train_data_file_path: str = os.path.join(ARTIFACTS_DIR, "train_data.csv")
    test_data_file_path: str = os.path.join(ARTIFACTS_DIR, "test_data.csv")

class DataIngestion: 
    def __init__(self, config: DataIngestionConfig): 
        self.config = config 

    def initiate_data_ingestion(self): 
        logging.info("Commencing data ingestion")
        try:
            # Read the raw data from the file 
            df = pd.read_csv(r"C:\Users\KIIT\Desktop\Data - Science\Electricity-Bill-Predictor\notebook\electricity_bill_dataset.csv")

            logging.info("Successfully read the data")

            # create a directory train data 
            os.makedirs(os.path.dirname(self.config.train_data_file_path), exist_ok=True)
            
            # save the dataframe to the raw data path
            df.to_csv(self.config.raw_data_file_path, index=False, header=True)
            logging.info("Successfully created the raw data directory")

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)
            logging.info("Successfully split the data")

            # split the data into train and test data 
            train_set.to_csv(self.config.train_data_file_path, index=False, header=True)
            logging.info("Successfully created the train data directory")

            # Save the train data to the train data path 
            train_set.to_csv(self.config.train_data_file_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_file_path, index=False, header=True)
            logging.info("Successfully exited the data splitting process")

            # Return the paths to the tgrain and test data 
            return(
                self.config.train_data_file_path, 
                self.config.test_data_file_path, 
            )

        except Exception as e: 
            logging.info("Data ingestion failed")
            raise FileOperatorError(e, sys)

if __name__=="__main__": 
    # create the config object
    config = DataIngestionConfig()
    # Create the data ingestion object 
    obj = DataIngestion(config)
    # Initiate the data ingestion 
    obj.initiate_data_ingestion()
    logging.info("Data ingestion completed successfully")

