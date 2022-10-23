import logging

from fastapi import FastAPI

from src.db import get_companies, get_summary, set_up_db

# set up logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s > %(funcName)s: %(message)s",
)

# Preparing database
set_up_db()

app = FastAPI()


@app.get("/")
def root():
    return "Hello Nuwe!"


@app.get("/companies")
def companies(sorted_by: str = None):

    return get_companies(sorted_by=sorted_by)


@app.get("/summary")
def summary():

    return get_summary()
