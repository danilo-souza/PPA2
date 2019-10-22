import sys
import Retirement_DB_Mock1, Retirement_DB_Stub, Retirement_DB_Mock2, Retirement_DB_Stub2

def test():
    global test_passed, test_failed

    if Retirement_DB_Mock1.canConnect():
        print("Can connect to the RETIREMENT database")
    if Retirement_DB_Mock2.canCloseDB():
        print("Can close connection to the RETIREMENT database")
    if Retirement_DB_Stub2.canAddEntry("test", "test", "test", "test", "test"):
        print("Can add entries to the retirement table")
    if Retirement_DB_Stub.canRetriveEntries() is not None:
        print("Can retrieve entries from the retirement table")

if __name__=="__main__":
    test()
