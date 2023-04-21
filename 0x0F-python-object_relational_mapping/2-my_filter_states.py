#!/usr/bin/python3
""" Write a script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where name
    matches the argument."""
if __name__ == '__main__':
    import MySQLdb
    import sys
    if len(sys.argv) == 5:
        try:
            db = MySQLdb.connect(
                    host='localhost', user=sys.argv[1], passwd=sys.argv[2],
                    db=sys.argv[3], port=3306)
        except MySQLdb.Error:
            pass
        try:
            cur = db.cursor()
            cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY states.id ASC".format(sys.argv[4]))
            entries = cur.fetchall()
            for item in entries:
                print(item)
        except MySQLdb.Error:
            pass
        cur.close()
        db.close()
