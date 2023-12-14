from confluent_kafka import Consumer, KafkaError
from time import time, sleep
from datetime import datetime

bootstrap_servers = 'localhost'
topic = 'test'

conf = {'bootstrap.servers': bootstrap_servers,
        'group.id': 'demo.hoonie',
        'auto.offset.reset': 'earliest'} 
consumer = Consumer(conf)
consumer.subscribe([topic])

try:
    while True:
        start_time = time()
        
        msg = consumer.poll(1.0) # Wait until the Message is Found
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print('Error - {}'.format(msg.error()))
                break

        print('Received message - {}'.format(msg.value().decode('utf-8')))
        
        end_time = time()
        sleep(1 - (end_time - start_time))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
    nowdate = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    print(f"Script Closed at {nowdate}.")
