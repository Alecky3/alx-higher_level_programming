#!/usr/bin/python3
"""Lists all 'cities' from the database 'hbtn_0e_4_usa'."""


if __name__ == "__main__":
    import MySQLdb
    import sys
    args = sys.argv[-4:]
    db = MySQLdb.connect(user=args[0], passwd=args[1], database=args[2])
    c = db.cursor()
    c.execute("""SELECT c.name,s.name FROM cities AS c
                 JOIN states AS s
                 ON s.id = c.state_id
                 ORDER BY c.id
             """)
    r = [name for name in c.fetchall() if name[1] == args[3]]
    count = 0
    for row in r:
        print(row[0], end="")
        count += 1
        if count + 1 <= len(r):
            print(", ", end="")

    print()
