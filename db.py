import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://shafinsiddique:Ishafin98@cluster0-jrksj.mongodb.net/<billiondollar>?retryWrites=true&w=majority")
main_db = client.get_database("billiondollar")

mentors_collection = main_db.get_collection("mentors")

students_collection = main_db.get_collection("students")

def updateName(email, new):
    foundUser = mentors_collection.find_one({'email': email})

    if foundUser:
        mentors_collection.update_one({'email': email}, {'$set': {'name': new}})


def updateHeader(email, new):
    return

def updateEmail(email, new):
    return

def updatePassword(email, new):
    return

def updateBio(email, new):
    return