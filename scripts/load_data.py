import json
import os
from pymongo import MongoClient


def load_data(mongo_uri=None, data_file=None):
    """Load sensor data from a JSON file into MongoDB."""

    mongo_uri = mongo_uri or os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongo_uri)
    db = client["sensor_data"]
    collection = db["readings"]

    default_path = os.path.join(os.path.dirname(__file__), '../data/sample_sensor_data.json')
    data_file = data_file or os.environ.get("DATA_FILE", default_path)

    with open(data_file, 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        result = collection.insert_many(data)
        inserted = len(result.inserted_ids)
    else:
        collection.insert_one(data)
        inserted = 1

    print("Data inserted successfully.")
    return inserted

if __name__ == "__main__":
    load_data()
