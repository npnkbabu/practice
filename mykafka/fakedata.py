from faker import Faker

fake = Faker()

def  get_registred_users():
    return{
        'name':fake.name(),
        'address':fake.address(),
        'created_at':fake.year()
    }