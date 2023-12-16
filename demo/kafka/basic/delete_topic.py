
def delete_topic(broker: str, name: str):
    from confluent_kafka.admin import AdminClient

    conf = {'bootstrap.servers': broker}
    client = AdminClient(conf)
    result = client.delete_topics([name])
    for topic, future in result.items():
        try:
            future.result()
            print(f"Topic '{topic}' deleted successfully.")
        except Exception as e:
            print(f"Failed to delete topic '{topic}': {e}")


if __name__ == "__main__":
    delete_topic(broker="localhost:9092",
                 name="created")