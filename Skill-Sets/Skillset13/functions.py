import math

def get_requirements():
    print("Temperature Conversion Program\n")
    print("\nProgram Requirements:\n"
          + "\n1. Program calculates sphere volume in liquid U.S. gallons from user-entered diameter value in inches, and rounds to two decimal places."
          + "\n2. Must use Python's *built-in* PI and pow() capabilities."
          + "\n3. Program checks for non-integers and non-numeric values."
          + "\n4. Program continues to prompt for user entry until no longer requested, prompt accepts upper or lower case letters.")
    print("Input:")


def isInteger(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def sphere_volume_calculator():
    answer = input("Do you want to calculate a sphere volume (y or n)? ")
    print("\nOutput:")


    if answer == "y" or answer == "Y":
        user_input = input("Please enter diameter in inches (integers only): ")
        if isInteger(user_input):
            radius = int(user_input) / 2
            volume = (4/3) * math.pi * math.pow(radius,3)
            gallons = round((volume / 231), 2)
            print("Sphere Volume: " + str(gallons) + " Liquid US Gallons")
            sphere_volume_calculator()             
        else:
            print("Incorrect entry. Please try again with an integer.")
            sphere_volume_calculator()

    if answer == "n" or answer == "N":
        print("Thank you for using our Sphere Volume Calculator!")