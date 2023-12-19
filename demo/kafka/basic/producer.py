import asyncio

def delivery_report(err, msg):
    if err is not None:
        print('Message Deliver Failed - {}'.format(err))
    else:
        print('Message Delivered - {} [{}]'.format(msg.topic(), msg.partition()))
        
        
def publish_message(broker:str, topic:str, key:str, message:str, partition:int=0):
    from confluent_kafka import Producer
    from time import time
    
    start_time = time()
    conf = {'bootstrap.servers': broker}
    producer = Producer(conf)
    producer.produce(topic, 
                     key=key,
                     partition=partition,
                     value=message, 
                     callback=delivery_report)
    producer.flush()
    for i in range(1, 1000):
        print("HELLO, KAFKA!")
    end_time = time()
    print(end_time-start_time)
    

if __name__ == "__main__": 
    pass
    