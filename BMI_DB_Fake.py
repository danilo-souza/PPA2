#A Fake to test database integration
from datetime import datetime

dit = {}

def addEntry(height, weight, output):
    global dit
    dit[str(height) + "\t" + str(weight)] = str(output) + "\t" + str(datetime.now())

def retrieveEntry():
    global dit
    output = "Height\tWeight\tOutput\tTime\n"
    for key in dit:
        output = output + key + "\t" + dit[key] + "\n"
    return output

def isEmpty():
    global dit
    return not bool(dit)

if __name__ == "__main__":
    if isEmpty():
        addEntry("5'6", "140", "Normal")
    retrieveEntries()

