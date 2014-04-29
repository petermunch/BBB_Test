__author__ = 'munchp'

from db_handler import db_init, db_insert_pit, db_insert_grill, db_insert_food, db_fetch_pit
from main import cookerSettings
import time
import random


def log_temperatures():

    #Insert dummy data in tables if we simulate
    if cookerSettings.simulate:
        db_insert_pit(random.randint(0, 500))
        db_insert_grill(random.randint(0, 300))
        db_insert_food(random.randint(0, 95))

        time.sleep(10)

        db_insert_pit(random.randint(0, 500))
        db_insert_grill(random.randint(0, 300))
        db_insert_food(random.randint(0, 95))