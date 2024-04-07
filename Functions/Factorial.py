#ITERATIVE
def factorial(n):
    for i in range(1, n):
        n = n*i
    return n

#RECURSIVE
#def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n * factorial(n-1)


n = int(input("Please enter a number to factorialize: "))
print(factorial(n))
