import json 

file_path = r'C:\Users\Tudor\Desktop\Python\Practice Python\birthdays.json'

birthdays = {}

with open(file_path, 'r') as file:
    data = json.load(file)

print("We currently know the birthdays of: ")
for item in data:
    print(item['name'])

print("----------------------------")
action = int(input("Would you like to:\n 1. See a Birthday\n 2. Add a Birthday\n"))

if action == 1:
    name = input("Whose birthday would you like to see? ")
    with open(file_path, 'r') as file:
        data = json.load(file)
    for item in data:
        if name == item['name']:
          print(f"{name}'s birthday is: {item['date']}")
elif action == 2:
    name = input("Whose birthday would you like to add? ")
    date = input("What's their birthday? ")
    new_entry = {"name": name, "date": date}
    print(f"Added the birthday of {name}, {date}.")
    
    with open(file_path, "r") as f:
        data = json.load(f)
    data.append(new_entry)
    
    with open(file_path, "w") as f:
        json.dump(data, f)

input("Press Enter to exit...")


