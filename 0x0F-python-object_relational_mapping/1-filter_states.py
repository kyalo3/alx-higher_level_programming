#!/usr/bin/python3

"""
a script that lists all states with a name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """parameters"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    "command line arguments"
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """print results in delimited format"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """connections close"""
    cursor.close()
    db.close()
