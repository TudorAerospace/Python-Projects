import random


a = ["🍇", "🍋", "🍒", "🍊", "🍉", "7"]
b = ["🍇", "🍋", "🍒", "🍊", "🍉", "7"]
c = ["🍇", "🍋", "🍒", "🍊", "🍉", "7"]
d = ["🍇", "🍋", "🍒", "🍊", "🍉", "7"]
e = ["🍇", "🍋", "🍒", "🍊", "🍉", "7"]
playing = True

while playing:
    f = random.randint(0, 5)
    print(a[f], end="")
    g = random.randint(0, 5)
    print(b[g], end="")
    h = random.randint(0,5)
    print(b[h], end="")
    i = random.randint(0,5)
    print(b[i], end="")
    j = random.randint(0,5)
    print(b[j], end="")

    print()
    if a == b and b == f:
        print("You win!")
    input("Press Enter to play again... ")
