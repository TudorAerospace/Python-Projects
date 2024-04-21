#Problem 9
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
print("\n".join(lines).upper())  # prints all lines
