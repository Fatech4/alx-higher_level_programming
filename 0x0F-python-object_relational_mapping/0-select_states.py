#!/usr/bin/python3
"""A module that connect to MySQL database and list all the states from the
hbtn_0e_0_usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    # check the number of arguments
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql username> <mysql password> <database name>".
            format(sys.argv[0])
            )
        exit(1)

    # connect to the database
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database: {}".format(e))
        exit(1)

    # execute the query to get all the states
    try:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("Error executing MySQL query: {}".format(e))
        exit(1)

    # close the database connection
    db.close()
