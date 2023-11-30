def get_requirements():
    print("Error Handling Program\n")
    print("\nProgram Requirements:\n"
          + "\n1. Program calculates two numbers, and rounds to two decimal places."
          + "\n2. Prompt user for two numbers, and a suitable operator."
          + "\n3. Use Python error handling to validate data."
          + "\n4. Test for correct arthimetic operator."
          + "\n5. Division by zero is not permitted."
          + "\n6. Note: Program loops until correct input entered - numbers and arthmetic operator."
          + "\n7. Replicate display below.")
    
def get_valid_float(pos):
    while True:
        try:
            num = float(input("\nEnter num" + str(pos) + ": "))
            return num
            break
        except ValueError:
            print("Not valid number!")
            continue

def get_valid_operator():
    print("\nSuitable Operators: +,-,*,/,// (integer division), % (modulo operator), ** (power)")

    op_list = ['+', '-', '*', '/', '//', '%', '**']
    op_test = input("Enter operator: ")

    while True:
        if op_test in op_list:
            return op_test
            break
        else:
            print("Incorrect operator!")
            op_test = input("\nEnter operator: ")
            continue

    

def error_handling():
    num1 = 0.0
    num2 = 0.0
    op = ''

    num1 = get_valid_float(1)
    num2 = get_valid_float(2)
    op = get_valid_operator()

    if op == "+":
        print("{0:,.2f}".format(num1 + num2))

    elif op == "-":
        print("{0:,.2f}".format(num1 - num2))
    elif op == '*':
        print("{0:,.2f}".format(num1 * num2))
    elif op == '/':
        while True:
            try:
                print("{0:,.2f}".format(num1 / num2))
                break
            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue
    elif op == '//':
        while True:
            try:
                print("{0:,.2f}".format(num1 // num2))
                break
            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == '%':
        while True:
            try:
                print("{0:,.2f}".format(num1 % num2))
                break
            except ZeroDivisionError as err:
                print("Cannot divide by zero!")
                num2 = get_valid_float(2)
                continue

    elif op == '**':
        print("{0:,.2f}".format(num1 ** num2))

    else:
        print("Incorrect Operator!")

    print("\nThank you for using our Math Calculator!")
    
