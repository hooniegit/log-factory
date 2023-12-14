from confluent_kafka import Producer
from time import time, sleep
from datetime import datetime

def delivery_report(err, msg):
    if err is not None:
        print('Message Deliver Failed - {}'.format(err))
    else:
        print('Message Delivered - {} [{}]'.format(msg.topic(), msg.partition()))

bootstrap_servers = 'localhost:9092'
topic = 'test'
conf = {'bootstrap.servers': bootstrap_servers}
producer = Producer(conf)

for i in range(1, 11):
    start_time = time()
    
    nowdate = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    message = f"DOHOON - nowdate is.. {nowdate}"
    producer.produce(topic, key=str(i), value=message, callback=delivery_report) # Produce Message
    producer.flush() # Send Produced Messages to Broker
    end_time = time()
    
    sleep(1 - (end_time - start_time))
