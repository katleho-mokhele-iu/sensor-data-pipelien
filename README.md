# Sensor Data Batch Storage Pipeline

This project implements a batch data storage system for environmental sensor data using MongoDB and Docker.

## Features
- Stores environmental telemetry data (temperature, humidity, air quality, etc.)
- Uses MongoDB as the backend database
- Containerized with Docker for portability and scalability
- Python script to load data in batch mode
- Easily deployable on local or cloud environments

## Project Structure
```
sensor_data_pipeline/
├── docker-compose.yml
├── mongo-init/
│ └── init.js
├── scripts/
│ └── load_data.py
├── data/
│ └── sample_sensor_data.json
└── README.md
```

## Getting Started

### Prerequisites
- Docker
- Python 3.x
- pip

### Steps to Run

1. Start MongoDB with Docker:
```bash
docker-compose up -d
```

2. Install Python dependencies:
```bash
pip install pymongo
```

3. Run the batch insert script:
```bash
python scripts/load_data.py
```

## Notes
- Ensure `sample_sensor_data.json` is in valid JSON format (as a list of documents).
- MongoDB runs locally on port 27017 and stores data in the `sensor_data.readings` collection.

## License
MIT