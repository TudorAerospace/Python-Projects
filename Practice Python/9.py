import random

print("Welcome to guessing game!")
print("The number is between 1 and 9")

num = random.randint(1,9)

game_over = False

a=0

while game_over == False:
    guess = int(input("Input your guess: "))
    if guess == num:
        print("You guessed correctly!")
        a = a+1
        game_over = True
    elif guess < num:
        print("Higher")
        a = a+1
    elif guess > num: 
        print("Lower")
        a = a+1
print(f"It took you {a} guesses to win!")