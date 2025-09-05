from src.network_security.exception.exception import CustomException
from src.network_security.logging.logger import logger
import os
import sys
import pymongo
import numpy as np
import pandas as pd

# configuring data_ingestion config
from src.network_security.entity.config_entity import DataIngestionConfig
from src.network_security.entity.artifact_entity import DataIngestionArtifact
from sklearn.model_selection import train_test_split

from dotenv import load_env
load_env()

MONGO_URL = os.getenv("Mongo_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_collection_as_dataframe(self):            # from mongo to df
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_URL)
            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop('_id',axis=1,inplace=True)

            df.replace({'na':np.nan},inplace=True)

            return df
        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_to_feature_store(self,dataframe:pd.DataFrame):
        feature_store_file_path = self.data_ingestion_config.feature_store_file_path

        dir_path = os.path.dirname(feature_store_file_path)
        os.makedirs(dir_path,exist_ok=True)

        dataframe.to_csv(feature_store_file_path,index=False,header=True)
        return dataframe

    def split_data_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)

            logger.info('train_test split successfull')
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True) 

            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)

            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
        
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_data_to_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)

            dataingestionartifact=DataIngestionArtifact(
                self.data_ingestion_config.training_file_path,
                self.data_ingestion_config.testing_file_path
            )
            return dataingestionartifact
        except Exception as e:
            raise CustomException(e,sys)

