f = open("test", "a")
f.write(input("Enter your text: "))
f.write(" ")
f.close()


f = open("test", "r")
print(f.read())

input("Press Enter to exit...")