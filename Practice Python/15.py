msg = str(input("Please input your message: "))
msg = msg.split(" ")
lgt = len(msg)

aux = msg[0]

for j in range(lgt-1):
    for i in range(0, lgt-j-1):
        aux = msg[i]
        msg[i] = msg[i+1]
        msg[i+1] = aux


print(msg)