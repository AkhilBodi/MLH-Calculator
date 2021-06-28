# A simple calculator to perform basic arthmetic.

# Prints the complete block
print("Please select the operator\n" \
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n")

operator = int(input("Selector your operator from 1, 2, 3, 4 : ")) # Asking user to select the desired operator

first_number = int(input("Enter your first number : "))
second_number = int(input("Enter your second number : "))

if operator == 1:
    print(first_number , "+", second_number, "=", first_number + second_number)  # Using the '+' operator to perform addition

elif operator == 2:
    print(first_number , "-", second_number, "=", first_number - second_number)  # Using the '-' operator to perform subtraction

elif operator == 3:
    print(first_number , "*", second_number, "=", first_number * second_number)  # Using the '*' operator to perform multiplication

elif operator == 4:
    print(first_number , "/", second_number, "=", first_number / second_number)  # Using the '/' operator to perform division

else:
    print("invalid input") # if the user entered a number other than the given selections.
