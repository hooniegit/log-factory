
def check_topic_partitions(broker:str, topic:str):
    from confluent_kafka.admin import AdminClient

    admin_conf = {'bootstrap.servers': broker}
    admin_client = AdminClient(admin_conf)
    topic_metadata = admin_client.list_topics(topic=topic).topics.get(topic)

    if topic_metadata:
        partition_count = len(topic_metadata.partitions)
        print(f'Topic "{topic}" has {partition_count} partitions.')
    else:
        print(f'Topic "{topic}" does not exist.')


if __name__ == "__main__":
    check_topic_partitions(broker="localhost:9092",
                           topic="sample_topic")