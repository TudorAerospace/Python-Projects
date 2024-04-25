#Problem 13
s = input("Enter your sentence: ")
dic = {'digits':0, 'letters':0}
s = list(s)
for i in s:
    if i.isalpha():
        dic['letters']+=1
    elif i.isdigit():
        dic['digits']+=1

for i in dic:
    print(i, ":", dic[i])