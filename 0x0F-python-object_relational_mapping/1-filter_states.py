#!/usr/bin/python3
""" A module for a script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa """
if __name__ == '__main__':
    import MySQLdb
    import sys
    if len(sys.argv) == 4:
        try:
            con = MySQLdb.connect(
                    host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                    port=3306, db=sys.argv[3]
                )
        except MySQLdb.Error:
            print("Kilosele")
            pass
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'\
                        ORDER BY states.id ASC"
                        )
            entries = cur.fetchall()
            for item in entries:
                print(item)
        except MySQLdb.Error:
            print("Wahala")
            pass
