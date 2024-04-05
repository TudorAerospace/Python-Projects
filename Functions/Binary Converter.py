print("Binary Number Converter")

def dec_to_bin(num):
    num = bin(num)[2:]
    return num

def bin_to_dec(num):
    num = str(num)
    num = int(num, 2)
    return num
    
num = 1001

num = bin_to_dec(num)

print(num)
