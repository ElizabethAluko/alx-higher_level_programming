#!/usr/bin/python3
"""Function that lists all cities from database"""

import MySQLdb
import sys


def main():
    """Lists al the cities from database"""

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_user,
            passwd=mysql_password, db=db_name
            )

    cur = db.cursor()
    cur.execute("SELECT cities.id,\
            cities.name, states.name FROM cities\
            INNER JOIN states ON\
            cities.state_id=states.id ORDER BY cities.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    main()
