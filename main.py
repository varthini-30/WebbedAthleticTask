import random

def guess(x):
    randomnumber = random.randint(1,x)
    guessnumber = 0
    while guessnumber != randomnumber:
        guessnumber = int(input(f"guess the number between (1,{x}):"))
        if guessnumber > randomnumber:
            print(f"the {guessnumber} is greater than com guess number")
        elif guessnumber < randomnumber:
            print(f"the {guessnumber} is smaller than com guess number")
    print(f"yaa yaa you won the game")

guess(10)