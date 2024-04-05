def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            pass
    if n == 2:
        return True
    
n = int(input("Input a number: "))
prime_status = is_prime(n)
print(f"Is {n} prime: {prime_status}")