#!/usr/bin/python3

"""
a script that displays all values in the
states table of database hbtn_0e_0_usa
where name matches the argument:
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """command line arguments"""
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]

    """connection to the database"""
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    query = "SELECT * FROM states WHERE  name LIKE BINARY %s ORDER BY id ASC"
    cursor = db.cursor()
    cursor.execute(query, (state,))

    """fetch all rows"""
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    """close connections in cursor and db"""
    cursor.close()
    db.close()
