import MySQLdb
from datetime import datetime

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root',
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS BMI")
    mydb.commit()

    cursor.execute("USE BMI")
    mydb.commit()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE bmi (height VARCHAR(10), weight VARCHAR(10), output VARCHAR(100), date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def canAddEntry(height, weight, output):
    setup()
    cursor.execute("INSERT INTO bmi VALUES(%s, %s, %s, %s)", (str(height), str(weight), str(output), str(datetime.now())))
    mydb.commit()
    cursor.close()
    mydb.close()
    return True

