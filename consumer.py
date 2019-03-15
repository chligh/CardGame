from kafka import KafkaConsumer

consumer = KafkaConsumer('test', group_id="123", bootstrap_servers=['127.0.0.1:9092,127.0.0.1:9093'])
for msg in consumer:
    recv = "topic:%s partition:%d offset:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print recv
