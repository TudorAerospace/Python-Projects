dictionary = { 'Vlad' : '01/05/2007', 'Stefan' : '03/08/2018', 'Tudor' : '21/10/2007'}

print("Welcome to the birthday dictionary! We know the birthdays of: ")

for key in dictionary:
    print(key)

name = str(input("Whose birthday would you like to look up? "))

print(name,"'s birthday is",dictionary[name])