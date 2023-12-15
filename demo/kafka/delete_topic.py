
# def delete_topic(broker:str, name:str):
#     from confluent_kafka.admin import AdminClient

#     try:
#         conf = {'bootstrap.servers': broker}
#         client = AdminClient(conf)
        
#         client.delete_topics([name])
    
#     except Exception as E:
#         print(f"ERROR APPEARD - {E}")

def delete_topic(broker: str, name: str):
    from confluent_kafka.admin import AdminClient

    conf = {'bootstrap.servers': broker}
    client = AdminClient(conf)

    # 토픽 삭제
    result = client.delete_topics([name])

    # 삭제 결과 확인
    for topic, future in result.items():
        try:
            future.result()
            print(f"Topic '{topic}' deleted successfully.")
        except Exception as e:
            print(f"Failed to delete topic '{topic}': {e}")



if __name__ == "__main__":
    delete_topic(broker="localhost:9092",
                 name="created")