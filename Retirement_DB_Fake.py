#A Fake to test database integration
from datetime import datetime

dit = {}

def addEntry(age, salary, percentage_saved, goal):
    global dit
    output = "sample"
    dit[str(datetime.now())] = str(age) + "\t" + str(salary) + "\t" + str(percentage_saved) + "\t\t" + str(goal) + "\t" + str(output)

def retrieveEntry():
    global dit
    output = "Age\tSalary\tPercentage\tGoal\tOutput\tTime\n"
    for key in dit:
        output = output + dit[key] + "\t" + key + "\n"
    return output

def isEmpty():
    global dit
    return not bool(dit)

if __name__ == "__main__":
    if isEmpty():
        addEntry("18", "20000", "10", "1,000,000", "never")
    retrieveEntries()

