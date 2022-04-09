#!/usr/bin/python3
"""
module
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    if not query_rows:
        print(end='')
    else:
        for row in query_rows:
            if row[1][0] == 'N':
                print(row)
    cur.close()
    db.close()
