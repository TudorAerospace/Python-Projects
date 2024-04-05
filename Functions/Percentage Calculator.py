print("Percentage Calculator")

for i in range(20000):
    type = int(input("Select the tool - (1) What is x% of y; (2) x is what percent of y ; (3) What is the percentage increase/decrease from x to y:"))
    if type in [1, 2, 3]:
        break
    else:
        print("Please input a value of 1, 2 or 3")
    
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if type == 1:
    z = x/100 * y
    print( round(z, 4), "is", x, "% of", y)
else:
    pass

if type == 2:
    z = (x/y) * 100 
    print (x, "is", round(z, 4), "% of", y)
else:
    pass

if type == 3:
    z = (y-x) / x * 100
    if x < y:
     print(x, "is a", round(z, 4), "% decrease from", y)
    elif y < x:
     print(x, "is a", round(z, 4), "% increase from", y)
    
else:
    pass

input("Press Enter to exit...")