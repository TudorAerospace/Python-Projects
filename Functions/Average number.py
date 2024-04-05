n = []
inputing = True
def calculate_average(n):
    lgth = len(n)
    a = 0
    for i in range(0, lgth):
        a += n[i]
    try:
        a /= lgth
        print(a)
    except ZeroDivisionError:
        print("You didn't input any numbers.")

print("Welcome to the average calculator!/n"
      "If write all of your numbers, then/n"
      "type 'done' to get the result.")

print("Input your numbers: ")
while inputing:n = []
inputing = True
def calculate_average(n):
    lgth = len(n)
    a = 0
    for i in range(0, lgth):
        a += n[i]
    try:
        a /= lgth
        return a
    except ZeroDivisionError:
        print("You didn't input any numbers.")

print("Welcome to the average calculator!/n"
      "If write all of your numbers, then/n"
      "type 'done' to get the result.")

print("Input your numbers: ")
while inputing:
    answer = 0
    answer = input()
    answer = answer.lower()
    if answer == "done":
        inputing = False
    else:
        try:
            answer = int(answer)
            n.append(answer)
        except ValueError:
            pass
    
n = calculate_average(n)

print(n)
    answer = 0
    answer = input()
    answer = answer.lower()
    if answer == "done":
        inputing = False
    else:
        try:
            answer = int(answer)
            n.append(answer)
        except ValueError:
            pass
    
calculate_average(n)
