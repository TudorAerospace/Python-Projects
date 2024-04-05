import random as rn
a=[]
b=[]

x = rn.randint(0, 10**2)
x = int(x)
y = rn.randint(0, 10**2)
y= int(y)
for i in range(x):
  a.append(rn.randint(0, 10**5))
for j in range(y):
  b.append(rn.randint(0, 10**5))
c = []
len_a = len(a)
len_b = len(b)
for j in range(len_a):
    for i in range(len_b):
        if a[j] in c:
           pass
        elif b[i] in c: 
           pass
        elif a[j] == b[i]:
          c.append(a[j]) 

if len(c) == 0:
   print("There are no common numbers")
else:
 print(c)

