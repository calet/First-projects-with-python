
message = "12<23<4>"
index1 = ""
index2 = ""
save = ""
for g in range(len(message)):
    save = message[g]
    if message[g] == '<':
        index1 = g
        for i in range(len(message[g:])):
            if i == '>':
                index2 = i
                
                
            for f in h[index1+1:index2]:
                combine += f
        
            for number, letter in alphabet.items():
                #turn number into letter
                if combine == str(number):
                    right_letter += letter
                    break
            combine = ""
            index1 = ""
            index2 = ""
