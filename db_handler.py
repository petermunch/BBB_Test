__author__ = 'munchp'

import sqlite3 as lite
import time

con = lite.connect('dbs/temps.db')


def db_init():

    with con:

        cur = con.cursor()
        cur.execute("CREATE TABLE Pit(Id INTEGER PRIMARY KEY, Time INT, Celcius REAL)")
        cur.execute("CREATE TABLE Grill(Id INTEGER PRIMARY KEY, Time INT, Celcius REAL)")
        cur.execute("CREATE TABLE Food(Id INTEGER PRIMARY KEY, Time INT, Celcius REAL)")

        print "Tables created successfully"


def db_insert_pit(temperature):
    t = time.asctime(time.localtime(time.time()))  # TODO: Set time to a smaller format, no need for date and year...

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Pit(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_insert_grill(temperature):
    t = time.asctime(time.localtime(time.time()))

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Grill(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_insert_food(temperature):
    t = time.asctime(time.localtime(time.time()))

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO Food(Time, Celcius) VALUES(?,?)", (t, temperature))
        print "Temperature added to db"


def db_fetch_pit():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Pit")

    rows = cur.fetchall()
    print "Data From Pit"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])


def db_fetch_grill():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Grill")

    rows = cur.fetchall()
    print "Data From Grill"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])


def db_fetch_food():

    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Food")

    rows = cur.fetchall()
    print "Data From Food"
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Time"], row["Celcius"])