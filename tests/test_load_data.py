import json
import os
import sys
from unittest import mock
import mongomock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts import load_data


def test_load_data_inserts_documents(tmp_path):
    sample = [{"a": 1}, {"b": 2}]
    data_file = tmp_path / "sample.json"
    data_file.write_text(json.dumps(sample))

    mock_client = mongomock.MongoClient()
    with mock.patch('scripts.load_data.MongoClient', return_value=mock_client):
        inserted = load_data.load_data(mongo_uri="mongodb://test", data_file=str(data_file))

    db = mock_client["sensor_data"]
    assert inserted == 2
    assert db["readings"].count_documents({}) == 2
