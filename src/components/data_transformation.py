import os 
import sys 
from dataclasses import dataclass 

import numpy as np 
import pandas as pd 

from src.exception import FileOperatorError
from src.logger import logging 

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Define a dataclass to hold the data transfomration configuration

@dataclass 
class DataTransformationConfig: 
    def __init__(self):
        preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.joblib")

# Define a dataclass to hold the data tranformation pipeline

@dataclass 
class DataTransformationline: 
    def __init__(self): 
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try: 
            # separate numerical and the categorize data
            # numerical_columns = self.data_transformation_config.numerical_columns
            num_columns = ['Fan', 'Refrigerator', 'Air Conditioner', 'Television', 'Monitor', 'Motor Pump', 'Month', 'Tariff Rate']
            cat_columns = ['City', 'Company']
            # Create a pipeline for numeric columns 
            num_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")), 
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    # Imputer
                    ("imputer", SimpleImputer(strategy="most_frequency")), 
                    # One Hot 
                    ("onehot", OneHotEncoder(handle_unknown="ignore")), 
                    # Scaler 
                    # "scaler", StandardScaler(with_mean=False)
                ]
            )
            logging.info("Data preprocessing complete")

            preprocessor = ColumnTransformer(
                transformers = [
                    ("num", num_pipeline, num_columns), 
                    ("cat", cat_pipeline, cat_columns)
                ]
            )

            logging.info(f"Preprocessor object: {preprocessor}")
            return preprocessor 
        
        except Exception as e: 
            raise FileOperatorError(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path): 
        try: 
            # Read the train and test data 
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Exited reading training and etsting datasets: ")            

            # Get the preprocessor object
            preprocessor_obj = self.get_data_transformer_obj()

            # Define the target variable 
            target_col = "Electricity_Bill"

        except Exception as e: 
            raise FileOperatorError(e, sys)