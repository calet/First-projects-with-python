from random import choice

lottery = ['a', 'h', '6', '1', 'f', 'u', '3', 'o', '9', '10', '2', '18', '13', '5', '7']
picked = 0
chosen = []
while picked < 4:
    chosen.append(choice(lottery))
    picked+=1
print("the winner is: " + ', '.join(chosen))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

my_ticket = ['a', 'a', 'a', 'a']
#my_ticket = []
my_chosen_ticket = []
all_tickets = 0
list_place = 0
alphabet_place = 0
counter = 0
list_times = 0
times_to_remove = 1
#while my_chosen_ticket != chosen:
while counter < 20:
    '''
    while list_place < 4 and alphabet_place < len(alphabet):
        my_ticket.insert(list_place, alphabet[alphabet_place])
        list_place+=1
    '''
    #list_place = 0
    if list_times == len(my_ticket):
        list_place = 0
        times_to_remove += 1
    if list_times == len(my_ticket):
        list_times = 0
    while alphabet_place < len(alphabet):
        
        for i in range(times_to_remove):
            del my_ticket[i]
            #my_ticket.pop(list_place)
        #for i in range(times_to_remove):
        for i in range(times_to_remove):
            my_ticket.insert(i, alphabet[alphabet_place])
        alphabet_place += 1
        print(my_ticket)

    '''
    point of program:
    aaaa
    1aaa
    2aaa
    3aaa
    .
    .
    bbbb
    1bbb
    .
    .
    a1aa
    b2bb
    etc
    '''
    times_to_remove += 1
    list_place += 1
    list_times += 1
    alphabet_place = 0
    counter+=1
    my_ticket = ['a', 'a', 'a', 'a']
    print()
