

def print_board():
    n = int(input("What board size would you like? "))
    for i in range(n):
        for i in range(n):
            print(" ---", end="")
        print()
        for i in range(n+1):
            print("|", end="   ")
        print()
    for i in range(n):
            print(" ---", end="")
    print()

print_board()