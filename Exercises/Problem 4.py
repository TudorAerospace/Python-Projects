#Problem 4
lst1 = str(input("Input your numbers, separated by a comma (,)"))
lst1 = lst1.split(',')
print(lst1)
lst2 = tuple(i for i in lst1)
print(lst2)