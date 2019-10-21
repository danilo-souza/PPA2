import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='danilo',
        database='BMI'
    )

    mydb.close()
    return True
