from ShortestDistance import shortest_distance

total_tests = 6
test_passed = 0
test_failed = 0

def output_test():
    global test_passed, test_failed

    #parameters
    point1 = (2, 3)
    point2 = (5, 6)

    output = shortest_distance(point1, point2)

    #testing if the calculations were done correctly
    if output == 4.243:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters
    point1 = (2, 11)
    point2 = (20, 6)

    output = shortest_distance(point1, point2)

    #testing if the calculations were done correctly
    if output == 18.682:
        print("\033[92m Output Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Output Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def input_test():
    global test_passed, test_failed

    #parameters, invalid x1
    point1 = ('a', 5)
    point2 = (4, 5)

    output = shortest_distance(point1, point2)
    if "Invalid x" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, invalid x2
    point1 = (3, 5)
    point2 = ('a', 5)

    output = shortest_distance(point1, point2)
    if "Invalid x" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, invalid y1
    point1 = (3, 'a')
    point2 = (4, 5)

    output = shortest_distance(point1, point2)
    if "Invalid y" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

    #parameters, invalid y2
    point1 = (3, 5)
    point2 = (4, 'a')

    output = shortest_distance(point1, point2)
    if "Invalid y" in str(output):
        print("\033[92m Input Test Passed. Output: ", output, "\033[0m")
        test_passed = test_passed + 1
    else:
        print("\033[91m Input Test Failed. Output: ", output, "\033[0m")
        test_failed = test_failed + 1

def stats():
    print(test_passed, "out of", total_tests, "tests passed")
    print(test_failed, "out of", total_tests, "tests failed")
    print(test_passed/total_tests * 100, "% of tests passed")