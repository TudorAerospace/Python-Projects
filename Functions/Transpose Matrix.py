
a = [[1, 2, 3, 3.5],
     [4, 5, 6, 6.5],
     [7, 8, 9, 9.5]]
def transpose_matrix(m):
    rez = []
    for i in range(len(m[0])):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        rez.append(row)
    for row in rez:
        print(row)

transpose_matrix(a)