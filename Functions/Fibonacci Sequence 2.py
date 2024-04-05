def fibonacci(n):
    a = 1
    b = 1
    c = 0
    lst = []
    if n == 0:
        lst = [0]
        return lst
    elif n == 1:
        lst = [0, 1]
        return lst
    elif n == 2:
        lst = [0, 1, 1]
    elif n > 2:
        lst.append(0)
        lst.append(a)
        lst.append(b)
        for i in range(n - 3):
            c = a
            a = a + b
            b = c
            lst.append(a)
    return lst

n = int(input("How many fibonacci numbers would you like to generate? "))
lst = fibonacci(n)
print(lst)
            


