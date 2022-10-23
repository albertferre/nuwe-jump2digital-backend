import json
import logging
from bson import json_util

import pymongo  # package for working with MongoDB

log = logging.getLogger(__name__)

def _get_collection():
    log.info("Connecting DB...")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]

    return collection


def set_up_db():

    collection = _get_collection()
    with open("data/companies.json", "r") as f:
        companies = json.load(f)
    log.info("Reset DB...")
    collection.delete_many({})  # reset DB
    log.info("Inserting data into DB...")
    collection.insert_many(companies)


def get_companies(sorted_by: str=None)->dict:
    """_summary_

    :param sorted_by: _description_
    :type sorted_by: str
    :raises ValueError: _description_
    :return: _description_
    :rtype: dict
    """
    if sorted_by not in ['founded', 'size'] and sorted_by is not None:
        raise ValueError(f"Invalid sorted_by argument: {sorted_by}")
    collection = _get_collection()

    cursor = collection.find({})

    companies = []
    for document in cursor:
        companies.append(document)

    response = json.loads(json_util.dumps(companies))
    
    if sorted_by == 'size':
        response = sorted(response, key=lambda d: (d[sorted_by] is None, d[sorted_by] == "", int(d[sorted_by].split('-')[0].replace('+', ''))))
    elif sorted_by == 'founded':
        response = sorted(response, key=lambda d: (d[sorted_by] is None, d[sorted_by] == "", d[sorted_by]))
    return response

