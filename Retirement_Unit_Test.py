from Retirement import retirement

total_tests = 11
test_passed = 0
test_failed = 0

def output_test():
    global test_passed, test_failed

    #parameters
    age = 20
    salary = 40000
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if output == 82:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed+=1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed+=1

    #parameters
    age = 20
    salary = 40000
    percentage_saved = 15
    goal = 1000000

    output = retirement(age, salary, percentage_saved, goal)

    if "Goal not reached" in str(output):
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed+=1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed+=1

def input_test():
    global test_passed, test_failed

    #paremeters, age invalid (negative)
    age = -1
    salary = 40000
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid age" in str(output):
        print("\033[92m Invalid Age Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Age Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #paremeters, age invalid (too old)
    age = 101
    salary = 40000
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid age" in str(output):
        print("\033[92m Invalid Age Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Age Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #paremeters, age invalid (not a number)
    age = 'a'
    salary = 40000
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid age" in str(output):
        print("\033[92m Invalid Age Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Age Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #parameters, salary invalid (negative salary)
    age = 20
    salary = -2
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid salary" in str(output):
        print("\033[92m Invalid Salary Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Salary Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    # parameters, salary invalid (not a number)
    age = 20
    salary = 'a'
    percentage_saved = 15
    goal = 500000

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid salary" in str(output):
        print("\033[92m Invalid Salary Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Salary Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #paremeters, percentage_saved invalid (negative)
    age = 20
    salary = 40000
    percentage_saved = -1
    goal = -100

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid percentage saved" in str(output):
        print("\033[92m Invalid Percentage Saved Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Percentage Saved Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    # paremeters, percentage_saved invalid (not a number)
    age = 20
    salary = 40000
    percentage_saved = 'a'
    goal = -100

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid percentage saved" in str(output):
        print("\033[92m Invalid Percentage Saved Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Percentage Saved Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #paremeters, goal invalid (negative)
    age = 20
    salary = 40000
    percentage_saved = 20
    goal = -100

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid goal" in str(output):
        print("\033[92m Invalid Goal Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Goal Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

    #paremeters, goal invalid (not a number)
    age = 20
    salary = 40000
    percentage_saved = 20
    goal = 'a'

    output = retirement(age, salary, percentage_saved, goal)

    if "Invalid goal" in str(output):
        print("\033[92m Invalid Goal Test Passed. Output: ", output, "\033[0m")
        test_passed += 1
    else:
        print("\033[91m Invalid Goal Test Failed. Output: ", output, "\033[0m")
        test_failed += 1

def stats():
    print(test_passed, "out of", total_tests, "tests passed")
    print(test_failed, "out of", total_tests, "tests failed")
    print(test_passed/total_tests * 100, "% of tests passed")