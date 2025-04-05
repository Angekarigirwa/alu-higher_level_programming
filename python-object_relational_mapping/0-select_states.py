#!/usr/bin/python3
"""script that lists all states"""
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
    cursor.execute("SELECT * FROM states ")
    states = cursor.fetchall()
    for state in states:
        print(state)
