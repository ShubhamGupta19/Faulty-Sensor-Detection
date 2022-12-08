from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__ == '__main__':
    training_pipeline_config=TrainingPipelineConfig()
    data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
    print(data_ingestion_config.__dict__)
    

