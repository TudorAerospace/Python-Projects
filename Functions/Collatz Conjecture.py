number = 0
steps = 0 

print("Collatz Conjecture Solver")

number = int(input("Enter a number: "))

def collatz(number):
   while number != 1:
      if number%2==0:
         number = number/2
         print("Number: " , number)
         steps = steps + 1
      elif number%2 == 1:
         number = number * 3 + 1
         print("Number: " , number)
         steps = steps + 1

   return steps

input("Press Enter to exit...")
