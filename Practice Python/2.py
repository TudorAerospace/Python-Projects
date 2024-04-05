number = int(input("Please enter your number: "))



if number % 4 == 0:
  print("Your number is a multiple of 4")
elif number % 2 == 1:
  print("Your number is odd")
elif number % 2 == 0:
  print("Your number is even")

num = int(input("Please enter your number: "))
check = int(input("Please enter your second number: "))

if num % check == 0:
  print("Your second number divides evenly in your first")
else:
  print("Your second number doesn't divide evenly in your first")