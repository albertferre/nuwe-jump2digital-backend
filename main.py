import logging
from fastapi import FastAPI

from src.db import get_companies, set_up_db

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
