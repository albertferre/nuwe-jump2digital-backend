import json
import logging

import pymongo  # package for working with MongoDB

log = logging.getLogger(__name__)


def set_up_db():
    log.info("Connecting DB...")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]

    with open("data/companies.json", "r") as f:
        companies = json.load(f)
    log.info("Reset DB...")
    collection.delete_many({})  # reset DB
    log.info("Inserting data into DB...")
    collection.insert_many(companies)


def get_companies(sorted_by: str = None):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]

    cursor = collection.find({}).sort([(sorted_by, pymongo.ASCENDING)])  # size

    companies = []
    for document in cursor:
        companies.append(document)

    return companies
