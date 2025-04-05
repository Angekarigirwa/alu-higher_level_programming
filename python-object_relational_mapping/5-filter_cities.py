#!/usr/bin/python3
"""list all cities of the state"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    state = sys.argv[4]
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        password=password,
        database=name
    )
    cursor = database.cursor()
    cursor.execute("SELECT cities.name, cities.id, states.name FROM cities \
        JOIN states ON cities.state_id=states.id WHERE states.name = %s \
            ORDER BY cities.id ASC", (state,))
    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))
