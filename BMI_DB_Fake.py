#A Fake to test database integration
from datetime import datetime

dit = {}

def addEntry(height_feet, height_inches, weight):
    global dit
    output = "sample"
    height = str(height_feet) + "'" + str(height_inches)
    dit[str(datetime.now())] = str(height) + "\t" + str(weight) + "\t" + str(output)

def retrieveEntry():
    global dit
    output = "Height\tWeight\tOutput\tTime\n"
    for key in dit:
        output = output + "\t" + dit[key] + key + "\n"
    return output

def isEmpty():
    global dit
    return not bool(dit)

if __name__ == "__main__":
    if isEmpty():
        addEntry("5'6", "140", "Normal")
    retrieveEntries()

