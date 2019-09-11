import math

def retirement(age, salary, percentage_saved, goal):
    try:
        age = int(age)

        if age < 0:
            return "Invalid age: Inputted age was less than 0"
        elif age >= 100:
            return "Invalid age: Inputted age was too old"
    except (TypeError, ValueError):
        return "Invalid age: Inputted age was not a number"

    try:
        salary = float(salary)

        if salary < 0:
            return "Invalid salary: Inputted salary was less than 0"
    except (TypeError, ValueError):
        return "Invalid salary: Inputted salary was not a number"

    try:
        percentage_saved = float(percentage_saved)

        if percentage_saved < 0:
            return "Invalid percentage saved: Inputted percentage saved was less than 0"
    except (TypeError, ValueError):
        return "Invalid percentage saved: Inputted percentage saved was not a number"

    try:
        goal = float(goal)

        if goal < 0:
            return "Invalid goal: Inputted goal was less than 0"
    except (TypeError, ValueError):
        return "Invalid goal: Inputted goal was not a number"


    #calculating annual savings
    personal_savings = salary * (percentage_saved/100)
    employer_match = personal_savings * 0.35
    annual_savings = personal_savings + employer_match

    #calculating how many years it would take
    delta_age = math.ceil(goal/annual_savings)
    final_age = age + delta_age

    if final_age >= 100:
        return ("Goal not reached. You would have to be " + str(final_age) + " to reach your goal")

    return final_age
