#Problem 15
inputing = True
while inputing:
    try:
        a = int(input("Please enter your digit: "))
        if len(str(a)) > 1:
            print("Please input only one digit") 
        else:
            inputing = False
    except ValueError:
        print("Please input a digit")

val = eval(f"{a}+{a}{a}+{a}{a}{a}+{a}{a}{a}{a}")
print(val)