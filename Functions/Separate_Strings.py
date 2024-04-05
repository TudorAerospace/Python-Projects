def separate_strings(n):
    numbers = []
    letters = []
    lst = []
    for item in n:
        lst.append(item)
    for i in range(len(lst)):
        if lst[i].isdigit():
            numbers.append(lst[i])
        if lst[i].isalpha():
            letters.append(lst[i])

    return letters, numbers
    

n = str(input())
a, b = separate_strings(n)

print(a, "\n")
print(b)
