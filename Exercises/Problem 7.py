#Problem 7
type_ = False
while not type_:
    try:
        i = int(input("Enter the first number: "))
        type_ = True
    except ValueError:
        print("Please input an integer")
type_ = False
while not type_:
    try:
        j = int(input("Enter the first number: "))
        type_ = True
    except ValueError:
        print("Please input an integer")

array = [[i*j for j in range(j)] for i in range(i)]

print(array)