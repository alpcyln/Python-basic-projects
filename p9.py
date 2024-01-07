## Calculator ##

run = True

def collection(x, y):
    total = int(x + y)
    print(total)

def extraction(x, y):
    total = x - y
    print(total)

def impact(x, y):
    total = x * y
    print(total)

def divide(x, y):
    total = x / y
    print(total)



while run:

    print("enter number:")

    x = int(input())

    print("select operator: +, -, x, /     Type exit to exit")

    operator = input()

    if operator == "+":
        print("enter number:")
        y = int(input())
        collection(x, y)


    if operator == "-":
        print("enter number:")
        y = int(input())
        extraction(x, y)

    if operator == "x":
        print("enter number:")
        y = int(input())
        impact(x, y)

    if operator == "/":
        print("enter number:")
        y = int(input())
        divide(x, y)

    if operator == "exit":
        print("You have logged out or logged in incorrectly")
        run = False

