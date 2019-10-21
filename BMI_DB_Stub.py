import MySQLdb

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

def canRetriveEntries():
    setup()
    print("Height\tWeight\tOutput\t\tDate")
    cursor.execute("SELECT * FROM bmi")
    result = cursor.fetchall()

    for tmp in result:
        print(tmp[0] + "\t" + tmp[1] + "\t" + tmp[2] + "\t" + tmp[3])

    cursor.close()
    mydb.close()
    return True
