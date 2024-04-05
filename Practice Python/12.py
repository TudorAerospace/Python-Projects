a = [5, 10, 15, 20, 25, 30]
b = []
def first_last():
    b.append(a[0])
    k = len(a)
    b.append(a[k-1])
    print(b)


first_last()