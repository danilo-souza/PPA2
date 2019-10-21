import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        password='password',
        database='RETIREMENT'
    )

    mydb.close()
    return True