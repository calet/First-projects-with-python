import time

message = "i got the high ground"
def forward():
     for i in range(len(message)+1):
        print(message[:i])
        time.sleep(.2)
def backwards():
    for i in range(len(message)+1):
        print(message[:-i-1])
        time.sleep(.2)
def left_right():
    for i in range(len(message)+1):
        print(" "*i + message[i:])
        time.sleep(.2)
def right_left():
    for i in range(len(message)+1):
        if i != 0:
            space = len(message)-i
            print(" "*space + message[-i:])
            time.sleep(.2)
def to_side():
    middle = int(len(message)/2)
    delete_right = ""
    delete_left = ""
    both = ""
    for i in range(len(message)):
        delete_right = message[middle:]
        delete_left = message[middle:]
        both = f" "*(middle+i) + f"{delete_left} {delete_right}"
        print(both)
        time.sleep(.2)
def droplets():
    #middle = int(len(message)/2)
    delete_right = ""
    delete_left = ""
    both = ""
    print('\n')
    for i in range(len(message)):
        delete_right = message[i:]
        delete_left = message[i:]
        #both = f" "*(middle+i) + f"{delete_left} {delete_right}"
        both = f" "*i + f"{delete_left} {delete_right}"
        print(both)
        print('\n')
        time.sleep(.3)
#donno what this does, wrote comment long after i made this
def donno():
    middle = int(len(message)/2)
    delete_right = ""
    delete_left = ""
    both = ""
    for i in range(len(message)):
        delete_right = message[middle:i+1]
        delete_left = message[middle:i+1]
        both = f"{delete_left}"+ " "*i+ f"{delete_right}"
        print(both)
        time.sleep(.2)
def idk():
    middle = int(len(message)/2)
    delete_right = ""
    delete_left = ""
    both = ""
    for i in range(len(message)):
        delete_right = message[middle+1:i+1]
        delete_left = message[middle+1:i+1]
        both = f"{delete_left}"+ " "*i +f"{delete_right}"
        print(both)
        time.sleep(.2)
#for i in range(2):
    #forward()
    #backwards()

for i in range(1):
    forward()
    backwards()
    right_left()
    left_right()
    to_side()
    for m in range(3):
        droplets()
    donno()
    idk()
    


    #for i in range(len(message)+1):

   