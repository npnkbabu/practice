from kafka import KafkaConsumer
import json



if __name__ == '__main__':
    consu = KafkaConsumer('registered_user_5'
                         ,bootstrap_servers=['localhost:9092']
                         ,auto_offset_reset='earliest'
                         ,group_id='consumer-group-a')
    print('starting consumer')
    for msg in consu:
        print(json.loads(msg.value))
    