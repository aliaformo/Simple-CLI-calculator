print("Welcome to this Simple CLI calculator program")
print("You will be able to add, subtract, multiply, divide or find the modulo for two numbers")
print("You will enter a first number, after that an operator and finally the second number")

simple_cli_calculator = True

while simple_cli_calculator:

    first_number = input("Enter the first number: ")
    needed_operator = input(
        "Enter an operator among these to perform the operation: +, -, /, *, %: ")
    second_number = input("Enter the second number: ")

    # Validating enter a number
    try:
        first_number == float(first_number)

        second_number == float(second_number)
    except:
        print("You should enter a number in each input")
        continue

    if needed_operator == "+":

        print("The sum is " + str(float(first_number) + float(second_number)))

    elif needed_operator == "-":

        print("The subtraction is " + str(float(first_number) - float(second_number)))

    elif needed_operator == "*":

        print("The product is " + str(float(first_number) * float(second_number)))

    elif needed_operator == "/":

        # Trying division by 0

        try:
            print("The division is " + str(float(first_number) / float(second_number)))
        except ZeroDivisionError:
            print("Division by 0 is invalid, try another denominator, please")

    elif needed_operator == "%":

        print("Modulo is " + str(float(first_number) % float(second_number)))

    # validating operators
    else:
        print("Please, try again picking a proper operator, it was an invalid operator entered")

    decision = input("Would you like to perform another operation, [y,n]: ")
    if decision == "y":
        continue
    elif decision == "n":
        simple_cli_calculator = False
    else:
        print("You should enter y or n")

print("Thanks for using this Simple CLI calculator program")






