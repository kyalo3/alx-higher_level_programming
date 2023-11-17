#!/usr/bin/python3

import MySQLdb
from sys import argv

"""arguments passed as parameters"""
user = argv[1]
passwd = argv[2]
db = argv[3]

if __name__ == "__main__":
    """command line arguments"""
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    """getting cursor and execution"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")

    """print results in delimited format"""
    rows = cursor.fetchall()

    """iterate the rows"""
    for row in rows:
        print(row)

    """close both dtabse and cursor"""
    cursor.close()
    db.close()
