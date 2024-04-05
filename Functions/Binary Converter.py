print("Binary Number Converter")

decimal = 0
binary = ""

for i in range(20000):
    type = int(input("Convert from Decimal(1) or Binary(0)? "))
    if type in [0, 1]:
        break
    else:
        print("Please input a value of 1 or 0")

if type == 1:
    decimal = int(input("Enter a decimal number: "))
    binary = bin(decimal)[2:]
elif type == 0:
    binary = input("Enter a binary number: ")

if type == 1:
    pass
elif type == 0:
    decimal = int(binary, 2)

print("Decimal number:", decimal)
print("Binary number:", binary)

input("Press Enter to exit...")
    

