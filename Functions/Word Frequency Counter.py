from collections import Counter

def word_frequency(n):
    punct = '''!()-[]{};:'".<>,/?@#$%^&*_~'''
    n = str(n)
    n = n.lower()
    for i in n:
        if i in punct:
            n = n.replace(i, "")
    n = n.split(" ")
    x = Counter(n)
    for key in x:
        print(key, ":", x[key])

n = input("Please input your sentence: ")
word_frequency(n)