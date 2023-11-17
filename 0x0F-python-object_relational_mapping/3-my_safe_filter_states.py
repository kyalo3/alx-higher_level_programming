#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    "command line arguments"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]

    "connection to my database"
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    query = ("SELECT * FROM states "
             "WHERE name LIKE BIMARY "
             "%s ORDER BY states.id ASC")

    cursor.execute(query, (state,))

    "fetch all the rows"
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    "close the cursor nd connection"
    cursor.close()
    db.close()
