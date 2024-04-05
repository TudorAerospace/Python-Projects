print("Permutation Left/Right")

for y in range(20000):
  direction = int(input("Which direction to permutate in; Left(0) or Right(1): "))
  if direction in [0, 1]:
    break
  else:
   print("Please input a value of either 0 or 1.")

n = int(input("Please enter the number of items in the list: "))

m = n

v=[0]*n

for i in range(n):
  v[i] = int(input("Enter list item {}: ".format(i)))

if direction == 0:
  aux = v[0]
  for z in range(n-1):
      v[z] = v[z+1]
  v[n-1] = aux  
elif direction == 1:
  aux = v[n-1]
  n = range(n)
  for z in reversed(n):
     v[z] = v[z-1]
  v[0] = aux    

if direction == 0:
  print("List permutated to the left: ")
elif direction == 1:
  print("List permutated to the right: ")

for i in range(m):
  print(v[i])

input("Press Enter to exit...")