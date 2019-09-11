from BMI import BMI

total_tests = 7
test_passed = 0
test_failed = 0

def input_test():
    global test_passed, test_failed

    #test height upper bounds; height =< 9 feet, weight =< 1400 pounds
    height_feet = 9
    height_inches = 1
    weight = 1400

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Upper Bound Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Upper Bound Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    # test weight upper bounds; height =< 9 feet, weight =< 1400 pounds
    height_feet = 9
    height_inches = 0
    weight = 1401

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Upper Bound Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Upper Bound Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #testing height lower bounds; height >= 1 feet 9 inches, weight >= 4.7 pounds
    height_feet = 1
    height_inches = 8
    weight = 5

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Lower Bound Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Lower Bound Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #testing weight lower bounds; height >= 1 feet 9 inches, weight >= 4.7 pounds
    height_feet = 1
    height_inches = 9
    weight = 4

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Lower Bound Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Lower Bound Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #testing for the right input types
    height_feet = 'a'
    height_inches = 9
    weight = 4

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Input Type Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Type Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    height_feet = 5
    height_inches = 9
    weight = 'b'

    output = BMI(height_feet, height_inches, weight)

    if "Invalid parameter" in str(output):
        print("\033[92m Input Type Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Type Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def output_test():
    global test_passed, test_failed

    #checking if output is as expected with the given inputs
    height_feet = 5
    height_inches = 6
    weight = 140

    output = BMI(height_feet, height_inches, weight)

    if output == "Normal - 23.1":
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def stats():
    print(test_passed, "out of", total_tests, "tests passed")
    print(test_failed, "out of", total_tests, "tests failed")
    print(test_passed/total_tests * 100, "% of tests passed")