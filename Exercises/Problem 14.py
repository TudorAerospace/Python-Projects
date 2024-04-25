#Problem 14
msg = input("Please enter your sentence: ")
dic = {'upper case': 0, 'lower case': 0}
msg = list(msg)
for i in msg:
    if i.isupper():
        dic['upper case']+=1
    if i.islower():
        dic['lower case']+=1

for i in dic:
    print(i, ":", dic[i])