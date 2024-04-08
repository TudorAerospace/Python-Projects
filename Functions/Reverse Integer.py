#Reverse Integer

def reverse_int(num):
    num = str(num)
    num = list(num)
    j = len(num) - 1
    i = 0
    while j >= int(len(num)/2):
        if i == j:
            pass
        aux = num[j]
        num[j] = num[i]
        num[i] = aux
        j -= 1
        i += 1
    while num[0] == '0':
        del(num[0])
    return int(''.join(num))

num = 12334141400
print(reverse_int(num))