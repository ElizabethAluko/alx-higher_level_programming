#!/usr/bin/python3
"""Function that lists all cities from database"""

import MySQLdb
import sys


def main():
    """Lists al the cities from database"""

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_user,
            passwd=mysql_password, db=db_name
            )

    cur = db.cursor()
    cur.execute("SELECT name FROM cities WHERE state_id IN\
            (SELECT id FROM states WHERE name = %s)\
            ORDER BY cities.id", (state_name, ))
    rows = cur.fetchall()

    """for row in rows:"""
    print(', '.join([row[0] for row in rows]))

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
