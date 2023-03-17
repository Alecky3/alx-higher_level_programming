#!/usr/bin/python3
"""Takes an argument and displays all values in the 'states' tables
   with a 'name' matching the argument
   from the database 'hbtn_0e_0_usa'.
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    args = sys.argv[-4:]
    db = MySQLdb.connect(user=args[0], passwd=args[1], database=args[2])
    c = db.cursor()
    query = """SELECT id,name FROM states
               ORDER BY id
            """
    c.execute(query)
    r = c.fetchall()
    [print(row) for row in r if row[1] == args[3]]
