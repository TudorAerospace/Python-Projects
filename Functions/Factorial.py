def factorial(n):
    a = n
    i = 1
    for i in range(1, n):
        a = a*i
    return a

n = int(input("Please enter a number to factorialize: "))
fact = factorial(n)
print(fact)