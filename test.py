import pymongo
import pandas as pd
from sensor.configuration.mongodb_connection import MongoDBClient
import logging
mc=MongoDBClient(database_name="sensordata")
coll=mc.client["sensordata"]["fromkafkatopic"]
print()
df = pd.DataFrame(list(coll.find()))
print(df.columns)
# logging.info(df.columns)
print("this is mc")
# client = pymongo.MongoClient("mongodb+srv://user1:mypassword@sensortopic.fulcw0i.mongodb.net/?retryWrites=true&w=majority")
# collc=client["sensordata"]["fromkafkatopic"]
# print(collc)
# df = pd.DataFrame(list(collc.find()))
# print(df.columns)

