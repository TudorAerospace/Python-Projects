#Problem 18
v = "ABd1234@1"
v = list(v)
upper_case = False
lower_case = False
number = False
special = False
if len(v) >= 6 and len(v) <= 12:
    v = list(v)
    for i in v:
        if i.isalpha():
            if i.isupper():
                upper_case = True
            elif i.islower():
                lower_case = True
        elif i.isnumeric():
            number = True
        elif i == "@" or i == "#" or i == "$":
            special = True
if upper_case and lower_case and number and special:
    print(''.join(str(x) for x in v))