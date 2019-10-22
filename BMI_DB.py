import MySQLdb
from datetime import datetime

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='localhost',
        user='danilo',
        password='password',
        database='BMI'
    )

    cursor = mydb.cursor()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE bmi (height VARCHAR(10), weight VARCHAR(10), output VARCHAR(100), date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def addEntry(height, weight, output):
    cursor.execute("INSERT INTO bmi VALUES(%s, %s, %s, %s)", (str(height), str(weight), str(output), str(datetime.now())))
    mydb.commit()

def retriveEntries():
    output = ("Height\tWeight\tOutput\t\tDate\n")
    cursor.execute("SELECT * FROM bmi")
    result = cursor.fetchall()

    for tmp in result:
        output = output + tmp[0] + "\t" + tmp[1] + "\t" + tmp[2] + "\t" + tmp[3] + "\n"

    print(output)
    return output

def isEmpty():
    x = cursor.execute("SELECT * FROM bmi")

    if x:
        return False
    else:
        return True

def closeDB():
    cursor.close()
    mydb.close()

if __name__ == "__main__":
    setup()
    closeDB()