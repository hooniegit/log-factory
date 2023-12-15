from confluent_kafka.admin import AdminClient

admin_conf = {'bootstrap.servers': 'localhost:9092'}
admin_client = AdminClient(admin_conf)

topic_name = 'created'
topic_metadata = admin_client.list_topics(topic=topic_name).topics.get(topic_name)

if topic_metadata:
    partition_count = len(topic_metadata.partitions)
    print(f'Topic "{topic_name}" has {partition_count} partitions.')
else:
    print(f'Topic "{topic_name}" does not exist.')
