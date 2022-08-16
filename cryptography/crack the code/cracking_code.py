from random import choice

class Amount:
    def __init__(self):
        self.counting = 0
    
    def c(self):
        self.counting+=1

def alphabet(chosen, i, tries):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    h = 0
    
    while h < len(alphabet):
        letter_try = alphabet[h]
        tries.c()
        if tries.counting%1000 == 0:
            print(tries.counting)
        if letter_try != chosen[i]:
            h+=1
        else:
            return letter_try
        
def numbers(chosen, i, tries):
    number_try = 0
   
    c = int(chosen[i])
    while number_try < 19:
        if number_try == c:
            return number_try
        number_try+=1
        tries.c()
        if tries.counting%1000 == 0:
            print(tries.counting)

lottery = ['a', 'h', '6', '1', 'f', 'u', '3', 'o', '9', '10', '2', '18', '13', '5', '7']
picked = 0
chosen = []
while picked < 1000000:
    chosen.append(choice(lottery))
    picked+=1
print("the winner is: " + ', '.join(chosen))

my_chosen_ticket = []
all_tickets = 0
list_place = 0
alphabet_place = 0
counter = 0

list_times = 0

my_tries = Amount()
while counter < 4 and list_place < len(chosen):
    save_letter = alphabet(chosen, list_place, my_tries)

    if save_letter != None:
        my_chosen_ticket.append(save_letter)
    else:
        save_number = numbers(chosen, list_place, my_tries)
        my_chosen_ticket.append(save_number)
    
    list_place+=1
