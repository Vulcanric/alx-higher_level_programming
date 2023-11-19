#!/usr/bin/python3
"""
Contains a script that lists all cities from the database, `hbtn_0e_4_usa`
from the table, `cities`
with foreign key referenced to ids of state passed to cmdline argv[4]
(maps cities to their states)
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    statename = argv[4]

    list_cities = []

    db = MySQLdb.connect(
            host="localhost", port=3306, user=username, passwd=password,
            db=database
        )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = '{}'\
        ORDER BY cities.id ASC".format(statename)
            )

    cities = cursor.fetchall()

    for city in cities:
        list_cities.append(city[0])

    print(", ".join(list_cities))

    cursor.close()
    db.close
