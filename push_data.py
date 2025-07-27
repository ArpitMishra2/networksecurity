import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi    ##certify is used to verify the SSL certificate of the MongoDB connection ie https://docs.mongodb.com/manual/tutorial/verify-ssl-certificate/
ca=certifi.where() ##certifi.where() returns the path to the CA bundle file

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():    ##this is my ETL pipeline
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        """This function will be used to convert csv file to json format"""
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)  ##reset_index is used to reset the index of the dataframe
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records,database,collection): 
        """This function will be used to insert data into MongoDB"""
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__=='__main__':      ##execution of ETL pipeline
    FILE_PATH="Network_Data\phisingData.csv"  ##relative path of the csv file
    DATABASE="networksecurity"
    Collection="NetworkData"
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_records)