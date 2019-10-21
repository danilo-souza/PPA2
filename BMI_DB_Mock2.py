import MySQLdb

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='localhost',
        user='danilo',
        password='password',
        database='BMI'
    )

    cursor = mydb.cursor()

def canCloseDB():
    setup()
    cursor.close()
    mydb.close()
    return True
