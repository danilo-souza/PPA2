import MySQLdb

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root',
        database='BMI'
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS BMI")
    mydb.commit()

    cursor.execute("USE BMI")
    mydb.commit()


def canCloseDB():
    setup()
    cursor.close()
    mydb.close()
    return True
