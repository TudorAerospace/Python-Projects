print("Reverse Word Order")

string = str(input("Please enter your sentence: "))

result = string.split()

lght = len(result)

for j in range(lght - 1):
    for i in range(lght - 1 - j):
        aux = result[i]
        result[i] = result[i+1]
        result[i+1] = aux

print(result)
print("Word count: " , lght)

input("Press Enter to exit...")