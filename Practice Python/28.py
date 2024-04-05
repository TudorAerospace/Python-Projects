a = int(input("Please input your first number: "))
b = int(input("Please input your second number: "))
c = int(input("Please input your third number: "))

if b<a and c<a:
    print(a,"is the largest number")
elif a<b and c<b:
    print(b,"is the largest number")
elif a<c and b<c:
    print(c,"is the largest number")

input("Press Enter to exit...")