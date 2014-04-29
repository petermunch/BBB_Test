__author__ = 'munchp'

import sqlite3 as lite

con = lite.connect("dbs/settings.db")


class CookerSettingsClass():

    def __init__(self):
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM Cooker")
        row = cur.fetchone()
        self.pit_probe = row["Use Pit Probe"]
        self.simulate = row["Simulate"]
        self.send_mail = row["Send Mail"]

class RecipeSettingsClass():

    def __init__(self):
        con.row_factory = lite.Row

        cur = con.cursor()
        cur.execute("SELECT * FROM Recipes")
        row = cur.fetchone()
        self.name = row["Name"]
        self.grill_target = row["Grill Target"]
        self.food_target = row["Food Target"]
        self.cooking_time = row["Cooking Time"]