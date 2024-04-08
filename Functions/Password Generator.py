import random 
import pyperclip

def word_picker():
    file_path = r'C:\Users\Tudor\Desktop\Python\Practice Python\sowpods.txt'
    with open(file_path, 'r') as file:  
            word_to_get = file.readlines()
            word_to_get = random.choice(word_to_get)
            letters = list(word_to_get)
    return word_to_get, letters

def password_generator(strength):
      if strength == 1:
            password = (word_to_get, word_to_get_2)
            password = ''.join(word.strip().lower() for word in password)
            print(password)
            pyperclip.copy(password)
      elif strength == 2: 
            password = (word_to_get, word_to_get_2)
            password = ''.join(word.strip().lower() for word in password)
            num = random.randint(1,999)
            print(f"{password}{num}")
            pyperclip.copy(f"{password}{num}")
      elif strength == 3:
            password = (word_to_get, word_to_get_2)
            password = ''.join(word.strip().lower() for word in password)
            password = password.replace('b', 'B').replace('e','E').replace('z','Z').replace('j','J').replace('g','G').replace('o','0')
            rnd = random.randint(1,2)
            if rnd == 1:
                  password = password.replace('s','$')
            elif rnd == 2:
                  password = password.replace('d', '#')
            num = random.randint(1,999)
            print(f"{password}{num}")
            pyperclip.copy(f"{password}{num}") 

word_to_get,letters = word_picker()
word_to_get_2, letters = word_picker()

type_ = False
while not type_:
      try:
            strength = int(input("What password strength would you like: \n 1. Weak \n 2. Good \n 3. Excellent\n"))
            type_ = True
      except ValueError:
            print("Please input either 1, 2 or 3")

password_generator(strength)
input("Press Enter to exit...")
