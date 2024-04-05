print("Sort a list descending then ascending")

import numpy as np 

n = int(input("How many items are in your list? "))
lst1 = [0] * n

for x in range(n):
    lst1[x] = int(input("Enter list item {}: ".format(x)))

v = np.array(lst1)

lght = len(v)

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

print(v)
