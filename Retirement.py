import math
#import Retirement_DB_Fake, Retirement_DB_Mock1, Retirement_DB_Mock2, Retirement_DB_Stub
#import Retirement_DB

def retirement(age, salary, percentage_saved, goal):
    #Retirement_DB.setup()

    db_age = age
    db_salary = salary
    db_percentage_saved = percentage_saved
    db_goal = goal

    #if not Retirement_DB.isEmpty():
        #Retirement_DB_Mock2.retrieveEntries()
        #Retirement_DB_Fake.retrieveEntries()
        #Retirement_DB.retriveEntries()
    #else:
        #Retirement_DB_Stub.retrieveEntries()

    try:
        age = int(age)

        if age < 0:
            #addEntries(age, salary, percentage_saved, goal, "Invalid age: Inputted age was less than 0")
            return "Invalid age: Inputted age was less than 0"
        elif age >= 100:
            #addEntries(age, salary, percentage_saved, goal, "Invalid age: Inputted age was too old")
            return "Invalid age: Inputted age was too old"
    except (TypeError, ValueError):
        #addEntries(age, salary, percentage_saved, goal, "Invalid age: Inputted age was not a number")
        return "Invalid age: Inputted age was not a number"

    try:
        salary = float(salary)

        if salary < 0:
            #addEntries(age, salary, percentage_saved, goal, "Invalid salary: Inputted salary was less than 0")
            return "Invalid salary: Inputted salary was less than 0"
    except (TypeError, ValueError):
        #addEntries(age, salary, percentage_saved, goal, "Invalid salary: Inputted salary was not a number")
        return "Invalid salary: Inputted salary was not a number"

    try:
        percentage_saved = float(percentage_saved)

        if percentage_saved < 0:
            #addEntries(age, salary, percentage_saved, goal, "Invalid percentage saved: Inputted percentage saved was less than 0")
            return "Invalid percentage saved: Inputted percentage saved was less than 0"
    except (TypeError, ValueError):
        #addEntries(age, salary, percentage_saved, goal, "Invalid percentage saved: Inputted percentage saved was not a number")
        return "Invalid percentage saved: Inputted percentage saved was not a number"

    try:
        goal = float(goal)

        if goal < 0:
            #addEntries(age, salary, percentage_saved, goal, "Invalid goal: Inputted goal was less than 0")
            return "Invalid goal: Inputted goal was less than 0"
    except (TypeError, ValueError):
        #addEntries(age, salary, percentage_saved, goal)
        #addEntries(age, salary, percentage_saved, goal, "Invalid goal: Inputted goal was not a number")
        return "Invalid goal: Inputted goal was not a number"


    #calculating annual savings
    personal_savings = salary * (percentage_saved/100)
    employer_match = personal_savings * 0.35
    annual_savings = personal_savings + employer_match

    #calculating how many years it would take
    delta_age = math.ceil(goal/annual_savings)
    final_age = age + delta_age

    if final_age >= 100:
        tmp = "Goal not reached. You would have to be " + str(final_age) + " to reach your goal"
        #addEntries(age, salary, percentage_saved, goal, tmp)
        return tmp

    #addEntries(age, salary, percentage_saved, goal, final_age)

    return final_age

#def addEntries(age, salary, percentage_saved, goal, output):
    #Retirement_DB_Mock1.addEntry(age, salary, percentage_saved, goal, output)
    #Retirement_DB_Fake.addEntry(age, salary, percentage_saved, goal, output)
    #Retirement_DB.addEntry(age, salary, percentage_saved, goal, output)
    #Retirement_DB.closeDB()

if __name__=="__main__":
    print(retirement(10, 10, 10, 1000))
