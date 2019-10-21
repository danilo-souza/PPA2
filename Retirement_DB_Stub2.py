import MySQLdb
from datetime import datetime

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        password='password',
        database='RETIREMENT'
    )

    cursor = mydb.cursor()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE retirement (age VARCHAR(10), salary VARCHAR(100), percentage VARCHAR(5), goal VARCHAR(100),\
         output VARCHAR(100),\
        date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def canAddEntry(age, salary, percentage, goal, output):
    setup()
    cursor.execute("INSERT INTO retirement VALUES(%s, %s, %s, %s, %s, %s)", (str(age), str(salary), str(percentage), \
                                                                             str(goal), str(output),
                                                                             str(datetime.now())))
    mydb.commit()
    cursor.close()
    mydb.close()
    return True
