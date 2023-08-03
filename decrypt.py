# Enter the message to be decrypted:
encrypted = input("What is the encrypted code you want to decode? ")
decrypted = ""

for i in range(len(encrypted)):
# Change "*" to "a"
    if encrypted[i] == "*":
        decrypted += "a"
# Change "&" to "w"
    elif encrypted[i] == "&":
        decrypted += "e"
# Change "#" to "i"
    elif encrypted[i] == "#":
        decrypted += "i"
# Change "+" to "o"
    elif encrypted[i] == "+":
        decrypted += "o"
# Change "!" to "u"
    elif encrypted[i] == "!":
        decrypted += "u"
    else:
        decrypted += encrypted[i]
# print decoded message
print(decrypted)