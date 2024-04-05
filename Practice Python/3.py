n = int(input("Please enter the number of elements in your list: "))

a=[0]*n


for x in range(n):
    a[x] = int(input(f"Enter list item {x}: " ))

print("The numbers smaller than 5 in the list are: ")
for i in range(n):
    if a[i] < 5:
        print(a[i])