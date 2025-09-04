import os
import sys
import pandas as pd
import numpy as np

# Data ingestion constants
DATA_INGESTION_COLLECTION_NAME:str = "network_security"
DATA_INGESTION_DATABASE_NAME:str = "network_security_db"
DATA_INGESTION_DIR_NAME:str =  "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2


# Training pipeline constants
TARGET_COLUMN = 'Result'               # target variable
PIPELINE_NAME:str = 'NetworkSecurity'
ARTIFACTS_DIR:str = 'artifacts'
FILE_NAME:str = 'phisingData.csv'

TRAIN_FILE_PATH:str = 'train.csv'
TEST_FILE_PATH:str = 'test.csv'