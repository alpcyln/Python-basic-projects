## dice game ##

import random 
run = True
print("Type 1 to play the game:")
entry = input()
if entry == "1":
    while run:
        print("Type x to roll the dice and exit to exit.")
        commond = input()
        if commond == "x":
            print(random.randint(1,6))
        if commond == "exit":
            print("log out")
            run = False