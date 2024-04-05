n = int(input("What board size do you want? "))

for k in range(n):
    for i in range(n):
        print(" ---", end="")
    print()
    for j in range(n+1):
        print("|   ", end="")
    print()
for l in range(n):
    print(" ---", end="")
print()