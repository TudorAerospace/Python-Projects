#Two Sum

v = [2, 3, 11, 15, 7]
target = 9

def Two_Sum(v, target):
    for i in range(0, len(v)):
        for j in range(0, len(v)):
            if v[i] + v[j] == target:
                a = [i, j]
                return a

print(Two_Sum(v, target))