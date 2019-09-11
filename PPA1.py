import BMI
import Retirement
import ShortestDistance
import SplitTheTip
import sys

while True:
    print("Choose one of the options bellow:")
    print("1. Body Mass Index")
    print("2. Retirement")
    print("3. Shortest Distance")
    print("4. Split The Tip")
    print("5. Exit")

    choice = input(">")

    if int(choice) == 1:
        print("How tall are you? (in feet and inches. e.g. 5 11)")

        height = input(">")

        #splitting the height into feet and inches
        height = height.split(" ")
        height_feet = height[0]
        height_inches = height[1]

        print("What is your weight? (in pounds. e.g. 200)")
        weight = input(">")

        print("Your BMI is " + BMI.BMI(height_feet, height_inches, weight))

    elif int(choice) == 2:
        print("What is your current age?")
        age = input(">")
        print("What is your annual salary?")
        salary = input(">")
        print("What percentage of your salary do you save? (Input as a percentage not a decimal)")
        saving = input(">")
        print("How much money do you want to have by the time you retire?")
        goal = input(">")

        print("Retirement age:\n", Retirement.retirement(age, salary, saving, goal))

    elif int(choice) == 3:
        print("Input the first point. (Use the format (x, y))")
        point1 = input(">")
        print("Input the second point. (Use the format (x, y))")
        point2 = input(">")

        point1 = tuple(point1[1:-1].split(','))
        point2 = tuple(point2[1:-1].split(','))

        print(ShortestDistance.shortest_distance(point1, point2))

    elif int(choice) == 4:
        print("What was the total dinner amount without the tip?")
        dinner = input(">")
        print("How many guests are going to split the check?")
        guests = input(">")

        output = SplitTheTip.split_the_tip(dinner, guests)

        print(output)

    elif int(choice) == 5:
        print("Thank you for using this program!")
        sys.exit()

    else:
        print("Please choose a valid option.")