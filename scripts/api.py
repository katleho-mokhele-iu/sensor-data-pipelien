from flask import Flask, Response
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['sensor_data']
collection = db['readings']

@app.route('/readings', methods=['GET'])
def get_readings():
    docs = list(collection.find().limit(10))
    return Response(dumps(docs), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
