import random

print("Guessing Game 2!")

print("Think of a number.")
print("The computer will try to guess your number. If it's the right number, type <correct>, if it's too low, type <higher> and if it's too high, type <lower>.")

game_over = False
bot_guess = 50
print(f"My guess is {bot_guess}")

tries = 1
while game_over == False:
   answer = input("higher, lower or just right? ")
   if answer == "just right":
      game_over = True
   elif answer == "lower":
      bot_guess -= random.randint(1,25)
      while bot_guess < 0:
        bot_guess += random.randint(1,10) 
      print(f"My guess is {bot_guess}")
      tries += 1
   elif answer == "higher":
      bot_guess += random.randint(1,25)
      while bot_guess > 100:
        bot_guess -= random.randint(1,10) 
      print(f"My guess is {bot_guess}")
      tries += 1

print(f"Yay! I got it in {tries} tries!")

input("Press Enter to exit...")