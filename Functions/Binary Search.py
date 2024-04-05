v = [1, 7, 7, 3, 5, 6, 9, 5, 4]

def binary_search(v):
    found = False

    if len(v) == 0:
        n = int(input("Enter the number of elements: "))

        print("Please input the elements of your vector: \n")
        for i in range(n):
            a = int(input())
            v.append(a)

    n = len(v)
    for i in range(n):
        for j in range(n):
            if v[i] < v[j]:
                aux = v[j]
                v[j] = v[i]
                v[i] = aux

    x = int(input("What number would you like to search for? "))
    st = 0
    en = n

    while st <= en and found == False:
        mid = int((st + en)/2)
        if v[mid] == x:
            found = True
        if v[mid] < x:
            st = mid + 1
        if v[mid] > x:
            en = mid - 1

    if found == True:
        print(f"YES {v[mid]} is on position {mid}")
        return mid
    else:
        print("NO")

v = binary_search(v)

print(v)
