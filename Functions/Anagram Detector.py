#Anagram detector

def anagram(a, b):
    if len(a) != len(b):
        return False
    else:
        a, b = list(a), list(b)
        len_a = len(a)
        len_b = len(b)
        for i in range(0, len_a):
            for j in range(0, len_b):
                if a[i] == b[j]:
                    len_b -= 1
                    del(b[j])
                    break
        if len_b == 0:
            return True
        else:
            return False
                            
a = "tool"
b = "loot"

print(anagram(a, b))