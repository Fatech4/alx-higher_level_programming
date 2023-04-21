#!/usr/bin/env python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states ON cities.state_id = states.id")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
