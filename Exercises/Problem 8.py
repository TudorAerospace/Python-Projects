#Problem 8
string = str(input("Please enter your words, sepparated by a comma: "))
string = string.split(',')
string.sort()
print(','.join(string))