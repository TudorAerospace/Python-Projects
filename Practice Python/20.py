n = int(input("How many items are in your list? "))
lst1=[0]*n


for x in range(n):
    lst1[x] = int(input("Enter list item {}: ".format(x)))

a = int(input("Please enter another number: "))

lght = len(lst1)

for j in range(lght-1):
    for i in range(lght-1-j):
        if lst1[i] > lst1[i+1]:
           aux = lst1[i]
           lst1[i] = lst1[i+1]
           lst1[i+1] = aux

print(lst1)

for y in range(lght-1):
  b = lst1[y]
  truth_value = b == a


print(truth_value)