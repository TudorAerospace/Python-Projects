import random

number = random.randint(1, 9)
number_of_guesses = 0
guess = 0
while True:
	guess = 0
	while guess not in range(1,10):
		guess = int(input("Guess a number between 1 and 9: "))
		if guess in range(1, 10):
			number_of_guesses += 1
	if guess == number:
		break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")
