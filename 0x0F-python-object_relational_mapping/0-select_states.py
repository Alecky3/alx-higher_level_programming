#!/usr/bin/python3
"""Lists all 'states' from the database 'hbtn_0e_0_usa'."""


if __name__ == "__main__":
    import MySQLdb
    import sys
    args = sys.argv[-3:]
    db = MySQLdb.connect(user=args[0], passwd=args[1], database=args[2])
    c = db.cursor()
    c.execute("""SELECT id,name FROM states ORDER BY id""")
    r = c.fetchall()
    for r in r:
        print(r)
