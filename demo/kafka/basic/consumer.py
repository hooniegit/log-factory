
def consume_messages(broker:str, group_id:str, topic:str, key:str, partition:int=0):
    from confluent_kafka import Consumer, KafkaError
    
    conf = {
        'bootstrap.servers': broker,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            if msg.partition() == partition and msg.key() == key:
                print('Received message: {}'.format(msg.value().decode('utf-8')))

    except KeyboardInterrupt:
        pass
    
    finally:
        consumer.close()


if __name__ == '__main__':
    broker_address = 'localhost:9092'
    consumer_group_id = 'demo'
    kafka_topic = 'hoonie'
    target_key = "2"

    consume_messages(broker_address, consumer_group_id, kafka_topic, target_key)
