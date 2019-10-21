import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        password='p',
        database='BMI'
    )

    mydb.close()
    return True
