import random

print("Welcome to cows and bulls!")

num = random.randint(1000,9999)
num = str(num)
num = list(num)
game_over = False
num_guess = 0
while game_over == False:
    cows = 0
    bulls = 0
    guess = str(input("Input your guess: "))
    num_guess +=1
    a = guess
    guess = list(guess)
    for i in range(4):
        if guess[i] in num[i]:
            cows = cows+1
        else:
            bulls += 1
    print(f"Cows:{cows}")
    print(f"Bulls:{bulls}")
    if cows == 4:
        print(f"That's right! The number was {a}!")
        print(f"It took you {num_guess} guesses to get it right!")
        game_over = True
input("Press Enter to exit...")