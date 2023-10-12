def get_requirements():
    print("Square Feet to ")
    print("\nProgram Requirements:\n"
          + "1. Use python selection structure\n"
          + "2. Prompt user for two numbers\n"
          + "3. Test for numeric operator.\n"
          + "4. Display Below.\n")
    
def get_user_input():
    num1 = 0.0
    num2 = 0.0

    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    print("\nSuitable Operators: +,-,*,/,//(integer division), %(modulo), **(power)")
    op = input("Enter operator: ")

    return num1, num2, op

def print_selection_structures(num1, num2, op):
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "//":
        if num2 == 0:
            print("Cannot divide by zero!")
        else: 
            print(num1 // num2)
    elif op == "%":
        if num2 == 0:
            print("Cannot divide by zero!")
        else: 
            print(num1 % num2)
    elif op =="**":
        print("Using ** operator: " + str(num1 ** num2))
    else:
        print("Incorrect operator!")

