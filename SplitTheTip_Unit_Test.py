from SplitTheTip import split_the_tip

total_tests = 7
test_passed = 0
test_failed = 0

def output_test():
    global test_passed, test_failed

    #parameters
    dinner_amount = 55.40
    number_of_guests = 3

    output = split_the_tip(dinner_amount, number_of_guests)

    #testing output
    if "guest1 - 21.24 guest2 - 21.24 guest3 - 21.23" in output:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    ###################Second Input###############################
    #parameter
    dinner_amount = 15.16
    number_of_guests = 3

    output = split_the_tip(dinner_amount, number_of_guests)

    #testing output
    if "guest1 - 5.81 guest2 - 5.81 guest3 - 5.81" in output:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    ###################Third Input###############################
    #parameter
    dinner_amount = 45.98
    number_of_guests = 5

    output = split_the_tip(dinner_amount, number_of_guests)

    #testing output
    if "guest1 - 10.58 guest2 - 10.58 guest3 - 10.58 guest4 - 10.57 guest5 - 10.57" in output:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def input_test():
    global test_failed, test_passed

    #parameters, wrong dinner amount (negative number)
    dinner_amount = -10
    number_of_guests = 5

    output = split_the_tip(dinner_amount, number_of_guests)

    if "Invalid dinner amount" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, wrong dinner amount (not a number)
    dinner_amount = 'a'
    number_of_guests = 5

    output = split_the_tip(dinner_amount, number_of_guests)

    if "Invalid dinner amount" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, wrong number of guests (negative number)
    dinner_amount = 10
    number_of_guests = -2

    output = split_the_tip(dinner_amount, number_of_guests)

    if "Invalid number of guests" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, wrong number of guests (not a number)
    dinner_amount = 18
    number_of_guests = 'a'

    output = split_the_tip(dinner_amount, number_of_guests)

    if "Invalid number of guests" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def stats():
    print(test_passed, "out of", total_tests, "tests passed")
    print(test_failed, "out of", total_tests, "tests failed")
    print(test_passed/total_tests * 100, "% of tests passed")
    
    if test_failed > 0:
        sys.exit(1)
