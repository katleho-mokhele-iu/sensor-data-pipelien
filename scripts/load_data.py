import json
from pymongo import MongoClient
import os

def load_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["sensor_data"]
    collection = db["readings"]

    data_path = os.path.join(os.path.dirname(__file__), '../data/sample_sensor_data.json')
    with open(data_path, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print("Data inserted succesfully.")

if __name__ == "__main__":
    load_data()