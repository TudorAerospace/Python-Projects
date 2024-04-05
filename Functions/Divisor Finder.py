print("Divisor Finder")

number = int(input("Please enter your number: "))

is_prime = True

for x in range(2, number):
    if number % x == 0:
        is_prime = False
        print(x)

if is_prime == True:
  print("Your number is prime")

input("Press Enter to exit...")