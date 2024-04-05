n = int(input("How many Fibonnaci numbers would you like to generate? "))

def fibonnaci():
    b = [1, 1]
    for i in range(1, n): 
        b.append(b[i] + b[i-1])
    print(f"Your Fibonnaci Sequence is: {b}")

fibonnaci()