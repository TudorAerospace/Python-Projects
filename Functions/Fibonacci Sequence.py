print("Fibonnaci Sequence")

number = int(input("How many Fibonnaci numbers do you want to generate? "))

list = []

for i in range(0, number):
    if i == number:
        break
    list.append(i+1)
    list[0] = 1
    list.append(i+1)
    list[1] = 1
    list[i] = list[i] + list[i-1]

list = list[:number]

print(list)
    
input("Press Enter to exit...")
