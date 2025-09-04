import os
from datetime import datetime

from src.network_security.constant import training_pipeline

class TrainPipelineConfig:
    def __init__(self):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifacts_name = training_pipeline.ARTIFACTS_DIR

        self.artifacts_dir = os.path.join(self.artifacts_name,timestamp)

        self.timestamp:str = timestamp

class DataIngestionConfig:
    def __init__(self,train_pipeline_config:TrainPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(
            train_pipeline_config.artifacts_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )

        self.feature_store_file_path:str = os.path.join(
            self.data_ingestio_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME
        )

        self.training_file_path:str = os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TRAIN_FILE_PATH
        )

        self.testing_file_path:str = os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR,training_pipeline.TEST_FILE_PATH
        )

        self.train_test_split_ratio:float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = training_pipeline.DATA_INGESTION_DATABASE_NAME