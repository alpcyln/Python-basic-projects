## number guessing game ##
import random

run = True
print("If you want to play a guessing game, type start:")
start_commond = input()
if start_commond == "start":
    while run:
        run3 = True
        print("I kept a number between 1 and 100. guess.")
        x = random.randint(1,100)
        while run3:
            run2 = True
            guess = int(input())

            while run2:
                if x < guess:
                    print("less than the number you said")
                    run2 = False
                
                if x > guess:
                    print("more than the number you say")
                    run2 = False

                if x == guess:
                    print("you know right")
                    print("Type 1 to play again.")
                    print("Type exit to exit")
                    commond = input()
                    if commond == "exit":
                        run = False
                        run2 = False
                        run3 = False
                                            
                    if commond == "1":
                        run2 = False
                        run3 = False