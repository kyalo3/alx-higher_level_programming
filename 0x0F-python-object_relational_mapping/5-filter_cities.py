#!/usr/bin/python3

"""
a script that takes in the name of a state as an
argumenta and lists all cities of that state
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    """command line arguments"""
    db = MySQLdb.connect(port=3306,	user=argv[1], passwd=argv[2], db=argv[3])

    """getting cursor and execution"""
    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    """fetch all the rows"""
    rows = cursor.fetchall()

    """print the cities"""
    cities = ','.join(city[0] for city in rows)
    print(cities)

    """close the cursor and database"""
    cursor.close()
    db.close()
