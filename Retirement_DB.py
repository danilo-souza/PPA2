import MySQLdb
from datetime import datetime

def setup():
    global mydb, cursor
    mydb = MySQLdb.connect(
        host='localhost',
        user='danilo',
        password='password',
        database='RETIREMENT'
    )

    cursor = mydb.cursor()

    x = cursor.execute("SHOW TABLES")

    if x == 0:
        cursor.execute("CREATE TABLE retirement (age VARCHAR(10), salary VARCHAR(100), percentage VARCHAR(5), goal VARCHAR(100),\
         output VARCHAR(100),\
        date VARCHAR(100) PRIMARY KEY)")
        mydb.commit()

def addEntry(age, salary, percentage, goal, output):
    cursor.execute("INSERT INTO retirement VALUES(%s, %s, %s, %s, %s, %s)", (str(age), str(salary), str(percentage),\
                                                                             str(goal), str(output), str(datetime.now())))
    mydb.commit()

def retriveEntries():
    print("Age\tSalary\tPercentage\tGoal\t\tOutput\tTime")
    cursor.execute("SELECT * FROM retirement")
    result = cursor.fetchall()

    for tmp in result:
        print(tmp[0] + "\t" + tmp[1] + "\t" + tmp[2] + "\t\t" + tmp[3] + "\t" + tmp[4] + "\t" + tmp[5])

def isEmpty():
    x = cursor.execute("SELECT * FROM retirement")

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