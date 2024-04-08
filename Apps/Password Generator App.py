#Password Generator App

from tkinter import *
from pyperclip import *
from random import *

WIN = Tk()
WIN.title("Password Generator")
WIN.geometry("545x250")
WIN.resizable = False, False

def draw_buttons():
    button_weak = Button(WIN, text="Weak")
    button_weak.place(x=5, y=200)
    button_weak.config(width=20, height=2, cursor="hand2", command= lambda: button_clicked(1), bg= 'red', fg= 'white')

    button_med = Button(WIN, text="Medium")
    button_med.place(x=200, y=200)
    button_med.config(width=20, height=2, cursor="hand2", command= lambda: button_clicked(2), bg= 'yellow', fg= 'black')

    button_strong = Button(WIN, text="Strong")
    button_strong.place(x=390, y=200)
    button_strong.config(width=20, height=2, cursor="hand2", command= lambda: button_clicked(3), bg= 'green', fg= 'white')

Label(WIN, text=" ").grid(row=0, column=0)
Label(WIN, text="  Word 1: ").grid(row=1, column=0)
w_1 = Entry(WIN)
w_1.grid(row=1, column = 1)
Label(WIN, text=" ").grid(row=2, column=0)
Label(WIN, text="  Word 2: ").grid(row=3, column=0)
w_2 = Entry(WIN)
w_2.grid(row=3, column = 1)
Label(WIN, text=" ").grid(row=4, column=0)
Label(WIN, text="  Result: ").grid(row=5, column=0)
password_entry = Entry(WIN)
password_entry.grid(row= 5, column = 1)

def get_data():
   word_1 = w_1.get()
   word_2 = w_2.get()
   return word_1, word_2

def button_clicked(button_id):
    if button_id == 1:
        word_1, word_2 = get_data()
        password = (word_1, word_2)
        password = ''.join(word.strip().lower() for word in password)
        password = ''.join(choice([k.upper(), k ]) for k in password)
        copy(password)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    elif button_id == 2: 
        word_1, word_2 = get_data()
        password = (word_1, word_2)
        password = ''.join(word.strip().lower() for word in password)
        password = ''.join(choice([k.upper(), k ]) for k in password)
        num = randint(1,999)
        password = f"{password}{num}"
        copy(password)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    elif button_id == 3:
        word_1, word_2 = get_data()
        password = (word_1, word_2)
        password = ''.join(word.strip().lower() for word in password)
        password = password.replace('b', 'B').replace('e','E').replace('z','Z').replace('j','J').replace('g','G').replace('o','0').replace('a', '4')
        password = ''.join(choice([k.upper(), k ]) for k in password )
        rnd = randint(1,2)
        if rnd == 1:
            password = password.replace('s','$').replace('f', '&')
        elif rnd == 2:
            password = password.replace('d', '#').replace('i', '!')
        num = randint(1,999)
        password = f"{password}{num}"
        copy(password)
        password_entry.delete(0, END)
        password_entry.insert(0, password)
        

draw_buttons()

WIN.mainloop()