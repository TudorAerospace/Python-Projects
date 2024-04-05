import random as rn

random_a = [rn.randint(1, 100) for i in range(10)]

random_b = [rn.randint(1, 100) for i in range(10)]

print(f"Random list a: {random_a}")
print(f"Random list b: {random_b}")

equal = False

for j in range(1, 10):
    for i in range(1, 10):
        if random_a[j] == random_b[i]:
             print(f"The {j} item, {random_a[j]}, in a is equal to the {i} item , {random_b[i]}, in b")
             equal = True

if equal == True:
  pass
else:
  print("There are no common numbers in the lists.")