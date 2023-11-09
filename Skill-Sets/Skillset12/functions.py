def get_requirements():
    print("Temperature Conversion Program\n")
    print("\nProgram Requirements:\n"
          + "\n1. Program converts user-entered temperature into Fahrenheit to Celsius scales."
          + "\n2. Program continues to prompt for user entry until no longer requested."
          + "\n3. Note: upper or lower case letters permitted. Though, incorrect entries are not permitted."
          + "\n4. Note: Program does not validate numeric data (optional requirement).")
    print("Input:")
    

def temperature_conversion():
    temp_input = 0.0
    answer = input("Do you want to convert a temperature (y or n)? ")
    print("\nOutput:")

    if answer == "y" or answer == "Y":
        temp_type = input("Fahrenheit to Celcius? Type 'f', or Celcius to Fahrenheit? Type 'c': ")
        if temp_type == "f" or temp_type == "F":
            temp_input = float(input("Enter temperature in Fahrenheit: "))
            fahrenheit_to_celcius = (temp_input - 32) / 1.8
            print("Temperature in Celcius = " + str(fahrenheit_to_celcius))
            temperature_conversion()
                     
        elif temp_type == "c" or temp_type == "C":
            temp_input = float(input("Enter temperature in Celsius: "))
            celcius_to_fahrenheit = (temp_input * 1.8) + 32
            print("Temperature in Fahrenheit = " + str(celcius_to_fahrenheit))
            temperature_conversion()              
        else:
            print("Incorrect entry. Please try again.")
            temperature_conversion()

    if answer == "n" or answer == "N":
        print("Thank you for using our Temperature Conversion Program!")