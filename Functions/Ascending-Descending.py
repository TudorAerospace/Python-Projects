import numpy as np 

print("Sort a list descending then ascending")

n = int(input("How many items are in your list? "))
lst1 = [0] * n

try:
    for x in range(n):
        lst1[x] = int(input("Enter list item {}: ".format(x)))
except ValueError:
    print("Please input only numbers and try again.")
    for x in range(n):
        lst1[x] = int(input("Enter list item {}: ".format(x)))

v = np.array(lst1)

def ascending_descending(v):
    #first order the entire vector in ascending order

    lght = len(v)
    for j in range(int(lght)):
        for i in range(int(lght - j - 1)):
            if v[i] > v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux

    # Sort the first half of the array in ascending order
    for j in range(int(lght / 2)):
        for i in range(int(lght / 2 - j - 1)):
            if v[i] > v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux

    # Sort the second half of the array in descending order
    for j in range(int(lght / 2), lght - 1):
        for i in range(int(lght / 2), lght - 1):
            if v[i] < v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux

    return(v)

v = ascending_descending(v)

print(v)
