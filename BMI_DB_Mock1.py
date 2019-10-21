import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='localhost',
        user='danilo',
        password='password',
        database='BMI'
    )

    mydb.close()
    return True