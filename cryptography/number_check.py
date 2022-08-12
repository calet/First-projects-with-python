alphabet = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z',
    27: 'å',
    28: 'ä',
    29: 'ö'
}

#insert < > in numbers
message = input("write: ")
combine = ""
right_letter = ""

lenght = len(message)
for g in range(lenght):
    if message[g] == '<':
        index1 = g
        #index1 + 3 not correct
        index2 = message.find('>', index1, index1+3)

        for f in message[index1+1:index2]:
            combine += f
        #everything works but the number in < > gets printed
        
        for number, letter in alphabet.items():
            #turn number into letter
            if combine == str(number):
                right_letter += letter
                break
        g += index2
        combine = ""
        index1 = ""
        index2 = ""
    else:
        if message[g] == '>':
            continue
        else:
            right_letter += message[g]

print(right_letter)

#print non < > symbols/letters too

'''
this will only be to turn numbers into letters, 
this will be letter cryptation towards three main programs which will include the following:
-letter cryptation
-txt file cryptation
-guessing
-GUI for main program
main program is number_alphabet2 which combines all programs but without GUI
'''