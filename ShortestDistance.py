import math

def shortest_distance(point1, point2):
    try:
        deltaX = float(point2[0]) - float(point1[0])
    except (TypeError, ValueError):
        return "Invalid x value inputted."

    try:
        deltaY = float(point2[1]) - float(point1[1])
    except (TypeError, ValueError):
        return "Invalid y value inputted."

    #calculating distance and rounding at the third decimal point
    d = round(math.sqrt(deltaX**2 + deltaY**2), 3)

    return d
