print("Divisor Finder")

type_ = False
while not type_:
    try:
        num = int(input("Please enter your number: "))
        type_ = True
    except ValueError:
        print("Please input an integer")

def divisor_finder(num):
    is_prime = True
    divisors = []
    for x in range(2, num):
        if num % x == 0:
            is_prime = False
            divisors.append(x)
    if is_prime:
        return None
    else:
        return divisors

print(divisor_finder(num))

input("Press Enter to exit...")
