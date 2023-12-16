# 클러스터 노드 수 이상의 파티션은 생성할 수 없음

def create_topic(broker:str, name:str, partitions:int=1, replications:int=1):
    from confluent_kafka.admin import AdminClient, NewTopic

    conf = {'bootstrap.servers': broker}
    client = AdminClient(conf)

    topic = NewTopic(name, 
                     num_partitions=partitions,
                     replication_factor=replications)
    client.create_topics([topic])


if __name__ == "__main__":
    create_topic(broker="localhost:9092",
                 name="sample_topic")