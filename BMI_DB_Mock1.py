import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        password='password',
        database='BMI'
    )

    mydb.close()
    return True
