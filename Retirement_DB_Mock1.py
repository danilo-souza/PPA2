import MySQLdb

def canConnect():
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
    mydb.close()

    return True