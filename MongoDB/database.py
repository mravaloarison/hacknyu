from pymongo import MongoClient
<<<<<<< HEAD

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
=======
from datetime import datetime

# Connect to MongoDB (update the connection string as needed)
client = MongoClient("cluster0.06nr7.mongodb.net")
db = client["securityFilterDB"]
users_collection = db["users"]

# Check if a user with the username 'testuser0' already exists
existing_user = users_collection.find({"username": "testuser0"})

if existing_user.count() == 0:
    # Insert a new user if not found
    users_collection.insert_one({
        "username": "testuser0",
        "email": "test@testmail.com",
        "password_hash": "hashed_password_here",
        "created_at": datetime.now(),
        "last_login": datetime.now(),
        "is_active": True
    })
    print("User 'testuser0' added successfully")
else:
    print("User 'testuser0' already exists")

# Query for a user with the username 'user123'
query_user = users_collection.find({"username": "user123"})

# Print the query result as JSON
for user in query_user:
    print(user)
>>>>>>> 10cbe12b3906b6b3cb59bdce9070ed1a7322c813
