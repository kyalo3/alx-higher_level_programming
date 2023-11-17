#!/usr/bin/python3

"""
a script that lists all cities
from the database hbtn_0e_4_usa
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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    """fetch all the rows"""
    rows = cursor.fetchall()
    for city in rows:
        print(city)

    """close the cursor and database"""
    cursor.close()
    db.close()
