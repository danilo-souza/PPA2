import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root',
        database='BMI'
    )

    mydb.close()
    return True
