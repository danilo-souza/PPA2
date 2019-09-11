def BMI(height_feet, height_inches, weight):
    #Converting weight from pounds to kg, also checking if weight is a number
    try:
        weight = float(weight)
        weight_kg = weight * 0.45
    except (TypeError, ValueError):
        return "Invalid parameter: inputted weight is not a number"

    #Converting height from feet and inches to meters, also checking if the height is a number
    try:
        height_inches = float(height_inches)
        height_feet = float(height_feet)
        height_inches = (12 * height_feet) + height_inches
        height_meters = height_inches * 0.025
    except (TypeError, ValueError):
        return "Invalid parameter: inputted height is not a number"

    #Checking if height and weight follow the constraints
    if height_inches > 108:
        return "Invalid parameter: inputted height is too big"
    elif height_inches < 21:
        return "Invalid parameter: inputted height is too small"

    if weight > 1400:
        return "Invalid parameter: inputted weight is too big"
    elif weight < 4.7:
        return "Invalid parameter: inputted weight is too small"

    #doing the BMI math
    divisor = height_meters**2
    output = weight_kg/divisor

    #rounding the output to 2 decimal points
    output = round(output, 1)

    if output <= 18.5:
        output = "Undeweight  - " + str(output)
    elif output > 18.5 and output <= 24.9:
        output = "Normal - " + str(output)
    elif output > 25 and output <= 29.9:
        output = "Overweight - " + str(output)
    else:
        output = "Obese - " + str(output)

    return output
