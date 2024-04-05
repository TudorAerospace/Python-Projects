print("Calculator")

valid_operators = {"+", "-", "*", "/", "^"} 

for j in range(20000):
  operation = str(input("Please input your operation type (+ ; - ; * ; / ; ^): "))
  if operation in valid_operators:
     break
  else:
     print("Please input a correct operation type.")

c = 0
c = float(c)    

a = float(input("Please input first number: "))
b = float(input("Please input the second number: "))

if operation.__contains__("+"):
  c = a + b
elif operation.__contains__("-"):
  c = a - b 
elif operation.__contains__("*"):
  c = a * b 
elif operation.__contains__("/"):
  c = a / b
elif operation.__contains__("^"):
  b = int(b)
  e = a
  for p in range(b - 1):
    e = e * a
    c = e

print("Result: ", c)

valid_again = {"Y", "y", "yes", "1"}

for i in range(20000):
 again = str(input("Continue calculating with the result? (Y/N): "))
 if   again in valid_again:
            operation = str(input("Please input your operation type (+ ; - ; * ; / ; ^ ): "))
            print("First number: ", c)
            a = float(input("Please input the second number: "))
            if operation.__contains__("+"):
             d   = c + a
             c = d
             print("Result: ", d)
            elif operation.__contains__("-"):
             d = c - a 
             c = d
             print("Result: ", d)
            elif operation.__contains__("*"):
             d = c * a 
             c = d
             print("Result: ", d)
            elif operation.__contains__("/"):
             d = c / a
             c = d
             print("Result: ", d)
            elif operation.__contains__("^"):
              e = c
              a = int(a)
              for p in range(a - 1):
                e = e * c
                d = e
              print("Result: ", d)
              c = d
                
 else:
      print("Final Result:" ,d) 
      break
 
input("Press Enter to exit...")