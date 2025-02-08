from pymongo import MongoClient

client = MongoClient('mongodb+srv://dzheng4m:cGqGXWHSHFQRxSRZ@cluster0.06nr7.mongodb.net/')
database = client['SecurityFilterDb']
collection = db['users']

def add_user(username, password):
    user_data = {
        'username': username,
        'password': password,
        'email': email,
        'coin': coin
    }

    collection.insert_one(user_data)
    print("User added successfully")
