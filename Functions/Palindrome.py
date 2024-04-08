#Palindorme Checker

def is_palindrome(n):
    n = str(n).replace(' ', '')
    n = n.lower()
    l = len(n) - 1
    i = l
    j = 0
    pal = False
    while j < l/2: 
        while i > l/2:
            if n[j] == n[i]:
                pal = True
            else:
                return False
            i = i - 1
            j = j + 1
    if pal == True:
        return True

n = input("Enter a sentence: ")
print(is_palindrome(n))
