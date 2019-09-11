def check_3decimal(number):
    #checking if the input has more than 3 decimal places.
    #if the input only has 2 decimal places then round(number, 3) = round(number, 2)
    if not (round(number, 3) == round(number, 2)):
        #taking off the extra decimal digits
        number = (round(number - 0.005, 2))
        number = round(number + 0.01, 2)

    return number

def split_the_tip(amount, n):
    #adding the tip, rounding to the second decimal place
    try:
        amount = float(amount)
        if amount < 0:
            return "Invalid dinner amount inputted. A negative number was passed"
    except (TypeError, ValueError):
        return "Invalid dinner amount inputted. A value other than a number was passed"

    try:
        n = int(n)
        if n < 0:
            return "Invalid number of guests inputted. A negative number was passed"
    except (TypeError, ValueError):
        return "Invalid number of guests inputted. A value other than a number was passed"

    total_amount = round(amount * 1.15, 2)

    output = ''

    for i in range(0, n):
        #using rounding to make sure that the remaining number only goes up to 2 decimal places
        temp = round(check_3decimal(total_amount/(n-i)), 2)
        output = output + "guest" + str(i + 1) + " - " + str(temp) + " "
        total_amount-=temp

    return output
