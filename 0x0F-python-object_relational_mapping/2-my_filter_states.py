#!/usr/bin/python3
"""
Contains a script that queries a database for a list of rows
with `name` as the one passed to the cmdline from a table, `states`
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=username, passwd=password,
            db=database, charset='utf8'
            )

    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC".format(state)
            )

    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    db.close()
