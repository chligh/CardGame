import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='127.0.0.1:9093,127.0.0.1:9092')

producer.send('test', "fff")
producer.close()