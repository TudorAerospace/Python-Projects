#Problem 6
import math
C = 50
H = 30
Q = []

D = str(input("Please enter your numbers, separated by a comma: "))
D = D.split(',')

for i in D:
    Q.append(str(int(round(math.sqrt(2*C*float(i)/H)))))
print(','.join(Q))