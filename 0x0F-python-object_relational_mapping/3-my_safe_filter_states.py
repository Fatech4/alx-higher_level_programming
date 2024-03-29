#!/usr/bin/python3
""" write a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER\
            BY states.id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows as a list of tuples
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
