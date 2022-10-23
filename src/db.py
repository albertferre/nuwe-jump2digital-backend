import json
import logging
from collections import Counter, OrderedDict

import pymongo  # package for working with MongoDB
from bson import json_util

log = logging.getLogger(__name__)


def _get_collection():
    log.info("Connecting DB...")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["companiesDB"]
    collection = db["companies"]

    return collection


def set_up_db():
    """It saves all data in DB"""

    collection = _get_collection()
    with open("data/companies.json", "r") as f:
        companies = json.load(f)
    log.info("Reset DB...")
    collection.delete_many({})  # reset DB
    log.info("Inserting data into DB...")
    collection.insert_many(companies)


def get_companies(sorted_by: str = None) -> dict:
    """Companies list

    :param sorted_by: optional sorted by size or year founded
    :type sorted_by: str
    :raises ValueError: ValueError
    :return: companies list
    :rtype: dict
    """
    if sorted_by not in ["founded", "size"] and sorted_by is not None:
        raise ValueError(f"Invalid sorted_by argument: {sorted_by}")
    collection = _get_collection()

    cursor = collection.find({})

    companies = []
    for document in cursor:
        companies.append(document)

    response = json.loads(json_util.dumps(companies))

    if sorted_by == "size":
        response = sorted(
            response,
            key=lambda d: (
                d[sorted_by] is None,
                d[sorted_by] == "",
                int(d[sorted_by].split("-")[0].replace("+", "")),
            ),
        )
    elif sorted_by == "founded":
        response = sorted(
            response,
            key=lambda d: (d[sorted_by] is None, d[sorted_by] == "", d[sorted_by]),
        )
    return response


def get_summary() -> dict:
    """Summary companies data

    :return: Summary companies data
    :rtype: dict
    """
    companies = get_companies()

    size = Counter([x["size"] for x in companies])
    founded = Counter([x["founded"] for x in companies])
    industry = Counter([x["industry"] for x in companies])

    response = {
        "size": dict(OrderedDict(size.most_common())),
        "founded": dict(OrderedDict(founded.most_common())),
        "industry": dict(OrderedDict(industry.most_common())),
    }

    return response
