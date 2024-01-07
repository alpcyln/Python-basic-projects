## Program to display the larger of two numbers ##
print(int("First number:"))
x = input()
print(int("Second number:"))
y = input()

if x < y:
    print(f"{y} is greater than {x}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} and {y} are equal ")