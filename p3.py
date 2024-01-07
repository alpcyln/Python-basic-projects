#The function that performs the exponent operation##

print("First number:")
f_number = int(input())
print("Type 1 for addition, type 2 for subtraction, type 3 for multiplication.")
operator = int(input())
print("Second number:")
s_number = int(input())

if operator == 1:
    print(f_number + s_number)
elif operator == 2:
    print(f_number - s_number)
elif operator == 3:
    print(f_number * s_number)
else:
    print("hatalı giriş tekrar deneyiniz")
