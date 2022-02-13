import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient(
    "mongodb+srv://Arktyk:Arktyk@cluster0.pkk8t.mongodb.net/Test1?retryWrites=true&w=majority")
db_test = client.test

db = client["Test1"]
col = db["Collection1"]

dict = {"User1": "pw1", "User2": "pw2"}

test = col.insert_one(dict)
