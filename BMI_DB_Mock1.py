import MySQLdb

def canConnect():
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root',
    )

    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS BMI")
    mydb.commit()

    cursor.execute("USE BMI")
    mydb.commit()

    mydb.close()
    return True

if __name__ == "__main__":
    canConnect()