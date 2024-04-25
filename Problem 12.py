#Problem 12
values = []
v = [999, 1000, 2000, 2005, 1077, 2468, 1984, 2312, 4000]
for i in v:
    if i >= 1000 and i <= 3000:
        num = 0
        correct = True
        num = list(str(i))
        for j in num:
            if int(j) % 2 != 0:
                correct = False
        if correct:
            values.append(i)

print(values)