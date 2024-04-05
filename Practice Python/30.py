import random

def word_picker():
    file_path = r'C:\Users\Tudor\Desktop\Python\Practice Python\sowpods.txt'
    with open(file_path, 'r') as file:
    
            contents = file.readlines()
    print(random.choice(contents))

word_picker()
