from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:1234@cluster0.d6n08.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test

list = db.mydata
list.insert_one({"data":"test", "fwefwe":"fewfwef", "dict":{"test":"fwfwfwfwfewfe"}})