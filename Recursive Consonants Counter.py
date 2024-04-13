#Recursive Consonant Counter

def consonants(string, cons_count, n):
    string = list(string)
    if string is None or n == len(string):
        return cons_count
    elif string[n].lower() not in ["a", "e", "i", "o", "u"]:
        cons_count += 1
    return consonants(string, cons_count, n+1)

string = "coco"
print(consonants(string, 0, 0))