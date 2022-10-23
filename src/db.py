import json

import pymongo  # package for working with MongoDB


def set_up_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]

    with open("data/companies.json", "r") as f:
        companies = json.load(f)

    collection.insert_many(companies)

def get_companies(sorted_by:str=None):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]
    
    cursor = collection.find({}).sort([(sorted_by, pymongo.ASCENDING)]) #size

    companies = []
    for document in cursor:
          companies.append(document)

    return companies
