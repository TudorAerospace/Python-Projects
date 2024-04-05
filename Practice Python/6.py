
n = int(input("How many numbers in your list? "))

lst = [0]*n

for i in range(n):
  lst[i] = int(input(f"Enter list number {i} : "))

palindrome = True

for j in range(n):
  if lst[j] != lst [n-j-1]:
    palindrome = False


if palindrome == True:
  print("This string is a Palindrome")
else:
  print("This string is not a Palindrome")