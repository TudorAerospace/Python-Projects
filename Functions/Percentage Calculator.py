#Percentage Calculator

def x_prc_y(x, y): 
    z = x/100 * y
    return round(z, 4)

def x_is_what_prc_y(x, y):
    z = (x/y) * 100 
    return round(z, 4)

def prc_diff_x_y(x, y):
    z = (y-x) / x * 100
    return z

type_ = None
while type_ not in [0, 1, 2]:
    try:
        type_ = int(input("Would you like to calculate:\n0. What is x% of y?\n1. x is what % of y?\n2. % increase/decrease between x & y?\nEnter 0, 1, or 2: "))
    except ValueError:
        print("Please input either 0, 1, or 2\n")

correct_input = False
while not correct_input:
    try:
        x = int(input("Enter the value for x: "))
        correct_input = True
    except ValueError:
        print("Please input an integer")
correct_input = False
while not correct_input:
    try:
        y = int(input("Enter the value for y: "))
        correct_input = True
    except ValueError:
        print("Please input an integer")


if type_ == 0:
    result = x_prc_y(x, y)
elif type_ == 1:
    result = x_is_what_prc_y(x, y)
elif type_ == 2:
    result = prc_diff_x_y(x, y)

print(result)
