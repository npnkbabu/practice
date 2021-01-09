from kafka import KafkaProducer
import json
from faker import Faker
import time

fake = Faker()

def json_serializer(data):
    return json.dumps(data)

def get_data():
    return{
        'name':fake.name(),
        'address':fake.address(),
        'created_at':fake.year()
    }

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)
    print('started producer')
    count=20
    while(1==1):
        data = get_data()
        print(data)
        producer.send('testtopic',data)
        time.sleep(60)