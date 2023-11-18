#!/usr/bin/python3
"""
Contains a script that queries a database for a list of rows
with `name` starting with 'N' from a table `states`
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=username, passwd=password,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()
    for result in results:
        print(result)

    cursor.close()
    db.close()
