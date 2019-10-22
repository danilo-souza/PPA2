import sys
import BMI_DB_Mock1, BMI_DB_Stub, BMI_DB_Mock2, BMI_DB_Stub2

def test():
    global test_passed, test_failed

    if BMI_DB_Mock1.canConnect():
        print("Can connect to the BMI database")
    if BMI_DB_Mock2.canCloseDB():
        print("Can close connection to the BMI database")
    if BMI_DB_Stub2.canAddEntry("test", "test", "test"):
        print("Can add entries to the bmi table")
    if BMI_DB_Stub.canRetriveEntries() is not None:
        print("Can retrieve entries from the bmi table")

if __name__=="__main__":
    test()