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
def alphabet_loop(combined_number, my_letter):
    for number, letter in alphabet.items():
        #turn number into letter
        if combined_number == str(number):
            crypt.append(str(letter))
            combined_number = ""
            return letter
            
        #turn letter into number
        if my_letter == letter:
            crypt.append(str(number))
            return number
        if my_letter not in str(alphabet.keys()) and my_letter not in str(alphabet.values()) and my_letter != '<' and my_letter != '>':
            crypt.append(str(my_letter))
            return my_letter

message = ""
crypt = []
seperate = ""
combine = ""

while message != '   ':
    message = input("write something and turn it to numbers, or press space 3 times to quit: ")

    for h in message:
        index1 = message.find('<', message.index(h))
       
        index2 = message.find('>', index1)
        if h == message[index2] and index2-index1 == 1 or index2-index1 == 2:
            for f in message[index1+1:index2]:
                combine += f
            seperate += str(alphabet_loop(combine, h))
            #doesnt run
            if index2 == len(message):
                break
            combine = ""
            index1 = ""
            index2 = ""

        if h in alphabet.values():
            seperate += f"<{str(alphabet_loop(combine, h))}>"
        if h not in str(alphabet.keys()) and h not in str(alphabet.values()) and h != '<' and h != '>':
            seperate += alphabet_loop(combine, h)
    print(seperate)
    seperate = ""
    del crypt[:]

'''
first hand problems:
'''
#-number_check.py works but it outputs: <2><4>fg as bb67 instead of bd67 
#-if you write <5fi it only outputs 69 and not <5<6><9>
      
    
'''
second hand problems:
'''
#-fresh up
#-add test cases
#-fix countdown (doesnt work if you have two or more of same letter)
#-error handling?

#-write cryptic code instead of letters (this program is for both, but write individually too)
#-if two letters next to eachother in the guessing is correct take away the - sign
#-crypt a txt file
#-unlock letters on guessing

#(method)create alphabet
#(function)crypt sentence (this program)
#(function)decrypt sentence (other program)
#(function)guess cryptic or get meaning directly
#numbers of letters left

'''
this is main program for number/letter cipher.
there are two other programs which this is built on:
-letter cipher
built on (individually):
-letter cryptation
-txt file cryptation
-guessing

-number cipher
built on (individually):
-numbercryptation
-txt file cryptation
-guessing
'''
