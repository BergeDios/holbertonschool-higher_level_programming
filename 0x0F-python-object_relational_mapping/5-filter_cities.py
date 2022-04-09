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
    cur.execute("""SELECT cities.name
                 FROM states INNER JOIN cities
                 ON states.id = cities.state_id
                 WHERE states.name LIKE %s""", (argv[4],))
    query_rows = cur.fetchall()
    if not query_rows:
        print()
    for i, row in enumerate(query_rows):
        if i == len(query_rows) - 1:
            print("{}".format(row[0]))
        else:
            print("{}, ".format(row[0]), end='')
    cur.close()
    db.close()
