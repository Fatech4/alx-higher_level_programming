#!/usr/bin/python3
"""  A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor(MySQLdb.cursors.SSCursor)

        # Construct the SQL query
        query = "SELECT cities.name \
                FROM cities \
                INNER JOIN states \
                ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC"

        # Execute the query
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()
        separator = ", "

        result = ""
        result += separator.join(str(i[0]) for i in rows)
        print(result)

        # Close the database connection
        db.close()

    else:
        print("Usage: {} username password\
                database_name state_name".format(sys.argv[0]))
