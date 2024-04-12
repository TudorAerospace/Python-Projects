#Recursive GCD
def gcd(a, b):
    if b is 0:
        return a
    else:
        return gcd(b, a % b)
    
print(gcd(2, 20))