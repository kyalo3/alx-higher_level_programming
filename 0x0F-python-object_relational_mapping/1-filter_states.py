#!/usr/bin/python3

"""
a script that lists all states with a name
 starting with N (upper N) from the
database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """command line arguments"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    """connection to the database"""
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
