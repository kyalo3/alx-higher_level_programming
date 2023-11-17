#!/usr/bin/python3

import MySQLdb
from sys import argv

user = argv[1]
passwd = argv[2]
db = argv[3]

if __name__ == "__main__":
    "command line arguments"
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
