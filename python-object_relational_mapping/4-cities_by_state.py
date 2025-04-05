#!/usr/bin/python3
"""script that lists all cities from database by state"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user,
        password=password,
        database=name
    )
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM states, \
     cities WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    cities = cursor.fetchall()
    for city in cities:
        print(city)
