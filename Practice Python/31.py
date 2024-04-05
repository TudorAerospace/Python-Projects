word_to_guess = "EVAPORATE"
letters = list(word_to_guess)
print(letters)

def guessing():
    print("Welcome to Hangman!")
    a = len(word_to_guess)
    b = len(letters)
    guess_word = ["_ "]*a

    for i in range(20000):
        if "_ " in guess_word:
         print(''.join(guess_word))
         for i in range(20000):
           guess = input("Guess your leter: ")
           if guess in guess_word:
              print(f"You have already guessed {guess}.")
           else:
              break   
         for i in range(20000):
            if guess in word_to_guess:
                for i in range(a):
                    if guess in letters[i]:
                     guess_word[i] = guess
    print(f"Congratulations! You guessed the word: {''.join(guess_word)}")           





guessing()
