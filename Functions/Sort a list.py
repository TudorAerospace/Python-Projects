import numpy as np

print("List Sorter")

for i in range(20000):
    order = int(input("Order Ascending(0) or Descending(1)? "))
    if order in [0, 1]:
        break
    else:
        print("Please input a value of 0 or 1")

n = int(input("How many items are in your list? "))
lst1=[0]*n


for x in range(n):
    lst1[x] = int(input("Enter list item {}: ".format(x)))

lght = len(lst1)
v = np.array(lst1)

if order == 0:
 for j in range(lght - 1):
    for i in range(lght - 1 - j):
        if v[i] > v[i + 1]:
            aux = v[i]
            v[i] = v[i + 1]
            v[i + 1] = aux
else: 
    pass

if order == 1:
 for j in range(lght - 1):
    for i in range(lght - 1 - j):
        if v[i] < v[i + 1]:
            aux = v[i]
            v[i] = v[i + 1]
            v[i + 1] = aux
else: 
    pass



print(v)

input("Press Enter to exit...")