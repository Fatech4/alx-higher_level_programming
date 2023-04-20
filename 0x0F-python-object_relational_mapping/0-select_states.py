#!/usr/bin/python3
"""A module that connect to MySQL database and list all the states from the
hbtn_0e_0_usa database"""
if __name__ == '__main__':
    import MySQLdb

    db = MySQLdb.connect(
        host='localhost', user='root', passwd='', db='hbtn_0e_0_usa'
        )
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for elements in cur.fetchall():
        print(elements)
