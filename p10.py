## Bank ATM ##
run = True

x_balance = 500


def withdrax(x):
    global x_balance 
    if x_balance > x:
        new_balance = x_balance - x
        print(f"Withdraw ${x} from your account with ${x_balance}, Your remaining balance is ${new_balance}")
        x_balance = int(new_balance)
    else:
        print(f"insufficient funds, your balance is ${x_balance}")

def deposit(x):
    global x_balance
    new_balance = x_balance + x
    print(f"{x} dollars added to your account, your account of {x_balance} dollars became {new_balance} dollars")
    new_balance = x_balance

def balance():
    global x_balance
    print(f"Your balance is ${x_balance}")
    

print("Welcome to our ATM, type exit to exit your transaction. To go back, type back.Type yes to take action:")
commond = input()
if commond == "yes":
    while run:
        run2 = True
        print("enter your 4-digit card number:") 
        id_no = input()

        if id_no == "1234":
            
            while run2:
                run3 = True
                print("enter password:")
                password = input()
                if password != "1234":
                    print("Wrong password")
                if password == "1234":
                    while run3:
                        print("Select the action you want to perform")
                        print("Type 1 to withdraw money")
                        print("To deposit money, type 2")
                        print("Type 3 to see balance")
                        operator = input()
                        if operator == "1":
                            print("the amount you want to withdraw")
                            x = int(input())
                            withdrax(x)
                        if operator == "2":
                            print("The amount you want to deposit:")
                            x = int(input())
                            deposit(x)
                        if operator == "3":
                            balance()
                        if operator == "exit":
                            print("logged out")
                            run3 = False
                            run2 = False
                            run = False
                        
                        if operator == "back":
                            run3 = False

                if password == "exit":
                    print("logged out")
                    run = False
                    run2 = False

                if password == "back":
                    run2 = False
        else:
            print("logged out")
            run = False


