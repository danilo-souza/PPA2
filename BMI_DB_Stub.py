import MySQLdb

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root'
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS BMI")
    mydb.commit()

    cursor.execute("USE BMI")
    mydb.commit()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE bmi (height VARCHAR(10), weight VARCHAR(10), output VARCHAR(100), date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def canRetriveEntries():
    setup()
    output = "Height\tWeight\tOutput\tDate"
    cursor.execute("SELECT * FROM bmi")
    result = cursor.fetchall()

    for tmp in result:
        output = output + tmp[0] + "\t" + tmp[1] + "\t" + tmp[2] + "\t" + tmp[3] + "\n"

    cursor.close()
    mydb.close()
    return output
