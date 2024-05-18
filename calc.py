# Making a simple calcutor in python
# Taking inputs from the user
def float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

cycle_count = 0
continue_var = True

# Taking inputs from the user

while continue_var:
    num1 = float_input("Enter first number: ")
    while True:
        op = input("Enter operator: ")
        if op in ["+", "-", "*", "/", "end"]:
            break
        else:
            print("Invalid operator. Please enter a valid operator.")

        num2 = float_input("Enter second number: ")

    # Performing the calculation based on the operator
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    elif op == "end":
        break
    else:
        print("Invalid operator")

    # Printing the result
    print(f"Result: {result}")

    continueq = input(f"Do you want to continue? (y/n): ")
    continue_var = continueq != "n"

