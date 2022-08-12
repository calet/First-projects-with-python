class Calculator:
    def __init__(self):
        self.sum = 0
        self.dif = 0
        self.kv = 0
        self.pow = 0
        self.prod = 0 
        self.mod = 0
    def addition(self):
        not_add = True
        while not_add:
            print(f"\nyou have chosen: Addition")
            first_term = int(input("type a term: "))
            second_term = int(input("type a term: "))
            if second_term >= 0:
                self.sum = first_term + second_term
                not_add = False
            else:
                print("\nnot an addition!")

    def subtraction(self):
        not_sub = True
        while not_sub:
            print(f"\nyou have chosen: Subtraction")
            first_term = int(input("type a term: "))
            second_term = int(input("type a term (has to be negative): "))
            if second_term <= 0:
                self.dif = first_term + second_term
                not_sub = False
            else:
                print("\nnot a subtraction!")

    def division(self):
        print(f"\nyou have chosen: Division")
        numerator = int(input("type a numerator: "))
        denominator = int(input("type a denumerator: "))
        self.kv = numerator/denominator
           
    def multiplication(self):
        print(f"\nyou have chosen: Multiplication")
        first_factor = int(input("type a factor: "))
        second_factor = int(input("type a factor: "))
        self.prod = first_factor * second_factor

    def power(self):
        print(f"\nyou have chosen: Power")
        base = int(input("type a base: "))
        exponent = int(input("type a exponent: "))
        self.pow = base**exponent

    def modulation(self):
        print(f"\nyou have chosen: Modulation")
        numerator = int(input("type a numerator: "))
        denominator = int(input("type a denumerator: "))
        self.mod = numerator%denominator
    
    def display_calc(self, choices):
        calc_list = [self.sum, self.dif, self.kv, self.pow, self.prod, self.mod]
        for h in calc_list:
            if h:
                lap = calc_list.index(h)
                for key, value in choices:
                    if int(value)-1 == lap:
                        print(f"{key}: {h}")
                        h = 0
                        break
                break
def menu():
    choices = {
        "addition": '1',
        "subtraction": '2',
        "division": '3',
        "multiplication": '4',
        "power": '5',
        "modulation": '6',
        "quit": '7'
        }
    return choices

choice = ''
cho = menu()
while choice != 7:  
    print('')

    for cal, ch in cho.items():
        print(ch + '.', cal)

    choice = input("choose calculation method: ")

    calculate = Calculator()
    if choice == '1':
        cal = calculate.addition()
        calculate.display_calc(cho.items())

    if choice == '2':
        cal = calculate.subtraction()
        calculate.display_calc(cho.items())

    if choice == '3':
        cal = calculate.division()
        calculate.display_calc(cho.items())

    if choice == '4':
        cal = calculate.multiplication()
        calculate.display_calc(cho.items())

    if choice == '5':
        cal = calculate.power()
        calculate.display_calc(cho.items())

    if choice == '6':
        cal = calculate.modulation()
        calculate.display_calc(cho.items())