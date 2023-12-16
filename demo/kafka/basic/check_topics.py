
def check_topics(broker:str):
    from confluent_kafka.admin import AdminClient

    admin_conf = {'bootstrap.servers': broker}
    admin_client = AdminClient(admin_conf)

    topics = admin_client.list_topics().topics
    for topic_name, topic_metadata in topics.items():
        print(f"Topic: {topic_name}, Metadata: {topic_metadata}")


if __name__ == "__main__":
    check_topics("localhost:9092")