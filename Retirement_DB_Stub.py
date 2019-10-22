import MySQLdb

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='db',
        user='root',
        password='root'
    )

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS RETIREMENT")
    mydb.commit()

    cursor.execute("USE RETIREMENT")
    mydb.commit()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE retirement (age VARCHAR(10), salary VARCHAR(100), percentage VARCHAR(5), goal VARCHAR(100),\
         output VARCHAR(100),\
        date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def canRetriveEntries():
    setup()
    output = "Age\tSalary\tPercentage\tGoal\tOutput\tTime"
    cursor.execute("SELECT * FROM retirement")
    result = cursor.fetchall()

    for tmp in result:
        output = output + tmp[0] + "\t" + tmp[1] + "\t" + tmp[2] + "\t\t" + tmp[3] + "\t" + tmp[4] + "\t" + tmp[5] + "\n"

    cursor.close()
    mydb.close()
    return output
