import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

DBUSERNAME = os.getenv('DBUSERNAME')
DBPASSWORD = os.getenv('DBPASSWORD')

db = False

def __get_database():
    CONNECTION_STRING = f"mongodb+srv://{DBUSERNAME}:{DBPASSWORD}@cluster0.qrcbpl3.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)

    return client.get_database("ChineseBot")

def connect():
    global db
    db = __get_database()

def add_user(id: int):
    __get_database().get_collection("users").insert_one({"id": id})

def delete_user(id: int):
    __get_database().get_collection("users").delete_one({"id": id})

def user_exists(id : int):
    res = __get_database().get_collection("users").find_one({"id": id})
    return res != None

def get_users():
    return __get_database().get_collection("users").find()
