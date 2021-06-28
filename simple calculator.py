# def nat(a):
#     while a <= 100:
#         print(a)
#         a += 1

# nat(4)

print("Please select the operator\n" \
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n")

operator = int(input("Selector your operator from 1, 2, 3, 4 : "))

first_number = int(input("Enter your first number : "))
second_number = int(input("Enter your second number : "))

if operator == 1:
    print(first_number , "+", second_number, "=", first_number + second_number)

elif operator == 2:
    print(first_number , "-", second_number, "=", first_number - second_number)

elif operator == 3:
    print(first_number , "*", second_number, "=", first_number * second_number)

elif operator == 4:
    print(first_number , "/", second_number, "=", first_number / second_number)

else:
    print("invalid input")