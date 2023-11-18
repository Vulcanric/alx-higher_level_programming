#!/usr/bin/python3
"""
Contains a script that lists all cities from the database `hbtn_0e_4_usa`
table, `cities`
with foreign key referenced to ids of states (maps cities to their states)
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=database
        )

    cursor = db.cursor()
    cursor.execute(
    "SELECT cities.id, cities.name, states.name\
            FROM cities, states WHERE cities.state_id = states.id\
            ORDER BY cities.id ASC"
            )

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close
