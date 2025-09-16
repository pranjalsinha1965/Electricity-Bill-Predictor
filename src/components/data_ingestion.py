import os 
import sys 
from dataclasses import dataclass 

import pandas as pd 
from sklearn.model_selection import train_test_split 

from src.exception import FileOperatorError
from src.logger import logging 

@ dataclass 
class DataIngestionConfig: 
    # Define the default file path for row, testing and training values 
    raw_data_file_path: str = os.path.join('artifacts', raw_data.csv)
    traing_data_file_path: str = os.path.join('artifacts', train_data.csv)
    test_data_file_path: str = os.path.join('artifacts', test_data.csv)

class DataIngestion: 
    def __init__(self, config: DataIngestionConfig): 
        self.config = config 

    def initiate_data_ingestion(self): 
        logging.info("Commencing data ingestion")

