import MySQLdb

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root'
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS RETIREMENT")
    mydb.commit()

    cursor.execute("USE RETIREMENT")
    mydb.commit()

def canCloseDB():
    setup()
    cursor.close()
    mydb.close()
    return True
