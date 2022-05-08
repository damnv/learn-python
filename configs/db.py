from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://damnv:dam010919@cluster0.o8eal.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test

collection_user = db["test"]

collection_student = db["student"]
