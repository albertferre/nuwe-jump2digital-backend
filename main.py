import logging

from src.db import get_companies, set_up_db

# set up logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s > %(funcName)s: %(message)s",
)

if __name__ == "__main__":
    set_up_db()
