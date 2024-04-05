import random

def word_picker():
    file_path = r'C:\Users\Tudor\Desktop\Python\Practice Python\sowpods.txt'
    with open(file_path, 'r') as file:
    
            word_to_guess = file.readlines()
            word_to_guess = random.choice(word_to_guess)
            letters = list(word_to_guess)
    return word_to_guess, letters


def guessing():
    word_to_guess, letters = word_picker()
    a = len(word_to_guess)
    b = len(letters)
    b = b-1
    lives = 6
    guess_word = ["_ "]*b
    for i in range(20000):
     if lives == 0:
       break  
     if "_ " in guess_word:
         print(''.join(guess_word))
         for i in range(20000):
           guess = input("Guess your leter: ")
           if lives == 0:
             print(f"You have run out of guesses! The word was {word_to_guess}")
             break  
           elif guess in guess_word:
              print(f"You have already guessed {guess}.")
           elif guess not in letters:
              lives = lives-1
              print(f"The letter {guess} is incorrect. You have {lives} lives left.")
           else:
              break   
         for i in range(20000):
            if guess in word_to_guess:
                for i in range(a):
                    if guess in letters[i]:
                     guess_word[i] = guess
    if lives not in [0]:
       print(f"Congratulations! You guessed the word: {''.join(guess_word)}")


def main():
   print("Welcome to Hangman!")
   guessing()
   input("Press enter to exit...")
      
main()