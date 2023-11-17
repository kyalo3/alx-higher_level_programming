#!/usr/bin/python3

"""
lists all states in my database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    """command line arguments"""
    db = MySQLdb.connect(port=3306,	user=argv[1], passwd=argv[2], db=argv[3])

    """getting cursor and execution"""
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ")

    [print(state) for state in cursor.fetchall()]
