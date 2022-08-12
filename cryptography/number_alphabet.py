alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet.insert(0, None)

cryptic = []
decrypt = []
cryption = []
indices = []
newlist = []
savelist = []
#crypt sentence
message = input("Write a sentence or a word: ")
print(f"{', '.join(alphabet[1:])}\n")
for n in range(len(message)):
    if message[n] in alphabet:
        cryptic.append(alphabet.index(message[n]))
        if n+1 != len(message):
            if message[n+1] in alphabet:
                cryptic.append('-')
            else:
                cryptic.append('   ')
                continue
#decrypt numbers
for h in cryptic:
    if h != '-' and h != '   ':
        decrypt.append(alphabet[h])
    if h == '   ':
        decrypt.append(' ')
    else:
        continue

for g in range(len(decrypt)):
    if decrypt[g] != ' ':
        numberOfletters = g+1
    else:
        continue
print(f"CRYPTION: {''.join(map(str, cryptic))}")
print(f"numbers of letters: {numberOfletters}\n")
#choices to decrypt message
guess = input("want to guess or get meaning directly? G/D\n") 
print('\n')
if guess == 'D':
    print(f"DECRYPTION: {''.join(decrypt)}")
#change symbol to letter in cryptic on corresponding index as the letter
if guess == 'G':
    guessing = None
    while guessing != ''.join(decrypt) and cryptic != decrypt:
        guessing = input("\nGuess: ")
        print('\n')
        for i in guessing:
            numberOfletters = numberOfletters-1
            if i != ' ': 
                save = alphabet.index(i)
                if save in cryptic:
                    temp = alphabet[save]
                    swap = cryptic.index(save)
                    for h in guessing:
                        indices.append([i for i, c in enumerate(cryptic) if c == save])
                    for g in indices:
                        for j in g:
                            newlist.append(j)
            
                    for n in newlist:
                        cryptic[n] = temp
                        savelist.append(n)
                    del newlist[:]
                    del indices[:]
                    #for i in range(len(cryptic)):
                        #e = cryptic.index('-')
                else:
                    continue
                    
                for n in range(len(cryptic)):                  
                    if n+2 < len(cryptic):
                        if cryptic[n+1] == '-' and cryptic[n] in alphabet and cryptic[n+2] in alphabet:
                            del cryptic[n+1]
                        if cryptic[n+1] == '   ' and cryptic[n] in alphabet and cryptic[n+2] in alphabet:
                            cryptic[n+1] = ' '
                    else:
                        break

        print(f"{''.join(map(str, cryptic))}")
        print(f"number of letters left: {numberOfletters}\n")
        for s in range(len(guessing)):
            if guessing[s] not in decrypt:
                print("you guessed wrong!!\n")
            if guessing[s] in decrypt and cryptic != decrypt:
                print(f"the letter: {guessing[s]}, is correct, but still some to go!")

    print("congratulations you guessed right!!")
        
    
#turn alphabet into numbers and crypt/decrypt a message

'''
not done:
-FIRST-
-fresh up
-add funtions 
-add classes
-add test cases
-fix countdown (doesnt work if you have two or more of same letter)
-error handling

-AFTER-
-write cryptic code instead of letters
-if two letters next to eachother is correct take away the - sign
-crypt a txt file
-unlock letters on guessing
'''