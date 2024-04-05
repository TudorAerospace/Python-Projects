num = int(input("Please enter your number: "))

divisor = range(2, num)

for i in divisor:
    if num % i == 0:
        print(f"{i} is a divisor of {num}")
