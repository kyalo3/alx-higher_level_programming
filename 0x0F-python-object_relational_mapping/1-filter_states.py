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
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """fetch all rows"""
    rows = cursor.fetchall()

    for row in rows:
        if (row[1][0] == 'N'):
            print(row)

    """close connections in cursor and db"""
    cursor.close()
    db.close()
