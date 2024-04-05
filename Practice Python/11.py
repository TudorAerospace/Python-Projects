def prime():
    number = int(input("Please enter your number: "))
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False
    if is_prime == True:
        print("Your number is prime")
    elif is_prime == False:
        print("Your number is not prime")
    input("Press Enter to exit...")

prime()