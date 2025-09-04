import os
import sys

from dotenv import load_dotenv
load_dotenv()

mongo_URL = os.getenv('Mongo_URL')

import certifi          # https security
ca = certifi.where()    # list of SSL certificates

import pandas as pd
import numpy as np
import pymongo
from src.network_security.exception.exception import CustomException
from src.network_security.logging.logger import logger

class DataExtract:
    def __init__(self,database,collection):
        try:
            logger.info("Connecting to MongoDB ...")
            self.mongo_client = pymongo.MongoClient(mongo_URL, tlsCAFile=ca)
            
            self.database = self.mongo_client[database]
            self.collection = self.database[collection]

            logger.info("Successfully connected.")

        except Exception as e:
            raise CustomException(e,sys)
        
    
    def csv_to_mongo(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)

            records = data.to_dict(orient='records')
            self.collection.insert_many(records)

            logger.info(f"Inserted {len(records)} records into MongoDB")

            return len(records)
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = "data_source/phisingData.csv"
    DATABASE = 'net_security_db'
    COLLECTION = 'net_security'
    obj = DataExtract(DATABASE,COLLECTION)
    records_len = obj.csv_to_mongo(FILE_PATH)
    print(records_len)
