from pymongo import MongoClient
from confluent_kafka import Producer
import json
from bson import json_util

MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
MONGO_DB_NAME = "MusicModel"
MONGO_COLLECTION_NAME = "audio_features"

KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "musicdata"

mongo_client = MongoClient(MONGO_CONNECTION_STRING)
mongo_db = mongo_client[MONGO_DB_NAME]
mongo_collection = mongo_db[MONGO_COLLECTION_NAME]

kafka_producer = Producer({"bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS})

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Batch size for sending to Kafka
BATCH_SIZE = 100
batch = []

# Fetch data from MongoDB and publish to Kafka
for document in mongo_collection.find():
    batch.append(document)

    # If batch size is reached, send to Kafka
    if len(batch) >= BATCH_SIZE:
        # Convert batch to JSON and send to Kafka
        kafka_producer.produce(KAFKA_TOPIC, json.dumps(batch, default=json_util.default).encode('utf-8'), callback=delivery_report)

        # Clear batch
        batch = []

# Send remaining documents in batch
if batch:
    kafka_producer.produce(KAFKA_TOPIC, json.dumps(batch, default=json_util.default).encode('utf-8'), callback=delivery_report)

# Wait for all messages to be delivered
kafka_producer.flush()
