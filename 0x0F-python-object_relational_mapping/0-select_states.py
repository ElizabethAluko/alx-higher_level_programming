#!/usr/bin/python3
"""Contains a function that select states from database"""

import MySQLdb
import sys


def main():
    """
       Function to select all states from database
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_user,
            passwd=mysql_password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == '__main__':
    main()
