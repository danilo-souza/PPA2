#A Fake to test database integration
from datetime import datetime

dit = {}

def addEntry(age, salary, percentage_saved, goal, output):
    global dit
    dit[str(datetime.now())] = str(age) + "\t" + str(salary) + "\t" + str(percentage_saved) + "\t\t" + str(goal) + "\t" + str(output)

def retrieveEntries():
    global dit
    print("Age\tSalary\tPercentage\tGoal\t\tOutput\tTime")
    for key in dit:
        print(dit[key] + "\t" + key)

def isEmpty():
    global dit
    return not bool(dit)

if __name__ == "__main__":
    if isEmpty():
        addEntry("18", "20000", "10", "1,000,000", "never")
    retrieveEntries()
