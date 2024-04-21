#Problem 11
lst = str(input("Please enter your binary numbers, sepparated by a comma: "))
lst = lst.split(',')
dec = [int(i, 2) for i in lst]
final = [str(bin(i)) for i in dec if i%5 == 0]
print(','.join(final).replace("0b", ""))