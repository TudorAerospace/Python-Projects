#Problem 21
inputing = True
v = [0, 0]
while inputing:
    i = input("Please input your move: ")
    if i == "":
        inputing = False
    else:
        if "UP" in i.upper():
            i = i[2:]
            v[0] += int(i)
        elif "DOWN" in i.upper():
            i = i[4:]
            v[0] -= int(i)
        elif "RIGHT" in i.upper():
            i = i[5:]
            v[1] += int(i)
        elif "LEFT" in i.upper():
            i = i[4:]
            v[1] -= int(i)

print(v)