def is_prime(n):

    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            pass
    if n == 2:
        return True
    return True

type_ = False
while not type_:
    try:
        n = int(input("Input a number: "))
        type_ = True
    except ValueError:
        print("Please input an integer")

prime_status = is_prime(n)
print(f"Is {n} prime: {prime_status}")
