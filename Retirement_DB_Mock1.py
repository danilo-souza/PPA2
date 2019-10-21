import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='localhost',
        user='danilo',
        password='password',
        database='RETIREMENT'
    )

    mydb.close()
    return True