from kafka import KafkaProducer
from fakedata import get_registred_users
import json
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')
    
def get_partition(key,all_part,ava):
    return 0
    

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=json_serializer)
                        #,partitioner=get_partition)

if __name__ == '__main__':
    count = 30
    i=0
    while i < count:
        data = get_registred_users()
        print(data)
        producer.send('testtopic',data)
        time.sleep(4)
        i = i+1
