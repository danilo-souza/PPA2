import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        password='',
        database='RETIREMENT'
    )

    mydb.close()
    return True