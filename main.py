__author__ = 'munchp'

from load_settings import CookerSettingsClass, RecipeSettingsClass
from db_handler import db_init, db_fetch_pit, db_fetch_grill, db_fetch_food
from temperatures import log_temperatures
import time

init_done = True

while True:

    if not init_done:
        db_init()
        cookerSettings = CookerSettingsClass()
        recipeSettings = RecipeSettingsClass()
        init_done = True

    time.sleep(2)
    log_temperatures()

    db_fetch_pit()
    print ""
    db_fetch_grill()
    print ""
    db_fetch_food()

    exit(1)