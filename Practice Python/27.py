a =[[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]


for i in range(4):
    for j in range(20000):
     b = str(input("Please input Player X's position: "))
     c = b.split(",")
     d = int(c[0])
     e = int(c[1])
     if a[d][e] == 0:
        a[d][e] = "X"
        break
     else:
      print("Please use an empty space.")
    for row in a:
       print(' '.join(map(str, row)))
    for j in range(20000):
     b = str(input("Please input Player O's position: "))
     c = b.split(",")
     d = int(c[0])
     e = int(c[1])
     if a[d][e] == 0:
        a[d][e] = "O"
        break
     else:
      print("Please use an empty space.")
    for row in a:
       print(' '.join(map(str, row)))
