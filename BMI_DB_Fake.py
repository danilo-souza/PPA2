#A Fake to test database integration
from datetime import datetime

dit = {}

def addEntry(height, weight, output):
    global dit
    dit[str(height) + "\t" + str(weight)] = str(output) + "\t" + str(datetime.now())

def retrieveEntries():
    global dit
    print("Height\tWeight\tOutput\tTime")
    for key in dit:
        print(key + "\t" + dit[key])

def isEmpty():
    global dit
    return not bool(dit)

if __name__ == "__main__":
    if isEmpty():
        addEntry("5'6", "140", "Normal")
    retrieveEntries()

