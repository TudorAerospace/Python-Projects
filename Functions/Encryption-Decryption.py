print("Encryption/Decryption Code")

dictionary = {
    'a': '01', 'b': '10', 'c': '11', 'd': '100', 'e': '101',
    'f': '110', 'g': '111', 'h': '1000', 'i': '1001', 'j': '1010',
    'k': '1011', 'l': '1100', 'm': '1101', 'n': '1110', 'o': '1111',
    'p': '10000', 'q': '10001', 'r': '10010', 's': '10011', 't': '10100',
    'u': '10101', 'v': '10110', 'w': '10111', 'x': '11000', 'y': '11001',
    'z': '11010', 'A': '01', 'B': '10', 'C': '11', 'D': '100', 'E': '101',
    'F': '110', 'G': '111', 'H': '1000', 'I': '1001', 'J': '1010',
    'K': '1011', 'L': '1100', 'M': '1101', 'N': '1110', 'O': '1111',
    'P': '10000', 'Q': '10001', 'R': '10010', 'S': '10011', 'T': '10100',
    'U': '10101', 'V': '10110', 'W': '10111', 'X': '11000', 'Y': '11001',
    'Z': '11010', ' ': '00'
}

dictionary_opp = {
    '01': 'a', '10': 'b', '11': 'c', '100': 'd', '101': 'e',
    '110': 'f', '111': 'g', '1000': 'h', '1001': 'i', '1010': 'j',
    '1011': 'k', '1100': 'l', '1101': 'm', '1110': 'n', '1111': 'o',
    '10000': 'p', '10001': 'q', '10010': 'r', '10011': 's', '10100': 't',
    '10101': 'u', '10110': 'v', '10111': 'w', '11000': 'x', '11001': 'y',
    '11010': 'z', '00': ' '
}

for i in range(20000):
    type_of_op = int(input("Would you like to Encrypt(0) or Decrypt(1) a message?: "))
    if type_of_op in [0, 1]:
       break 
    else: 
        print("Please input either 0 or 1.")

message = str(input("Please input your message: "))

fct = [*message]

decr = message.split()

lgth_decr = len(decr)

lgth = len(fct)

value = 0

if type_of_op == 0:
  print("Encrypted message: ")
  for i in range(lgth):
     char_to_lookup = fct[i]
     value_for_char = dictionary[char_to_lookup]
     print(value_for_char,end=" ")
elif type_of_op == 1:
   print("Encrypted message: ")
   for j in range(lgth_decr):
      char_to_lookup = decr[j]
      value_for_char = dictionary_opp[char_to_lookup]
      print(value_for_char,end="")
     
 
input("\n Press Enter to exit...")