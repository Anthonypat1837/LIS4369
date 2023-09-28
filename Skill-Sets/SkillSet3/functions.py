def get_requirements():
    print("Square Feet to ")
    print("\nProgram Requirements:\n"
          + "1. Must use float data type for user input.\n"
          + "2. Find number of IT/ICT students in class.\n"
          + "3. Calculate IT/ICT Student Percentage.\n"
          + "4. Format, right-align numbers, and round to two decimals.")
    
def calculate_it_ict_student_percentage():
    it = 0
    ict = 0
    total_students = 0
    percent_it = 0.0
    percent_ict = 0.0

    print("Input: ")

    it = int(input("Enter number of IT students: "))
    ict = int(input("Enter number of ICT students: "))

    total_students = it + ict
    percent_it = it / total_students
    percent_ict = ict / total_students

    print("\nOutput")
    print("{0:17}{1:>5.2f}".format("Total Students", total_students))
    print("{0:17}{1:>5.2f}".format("IT Students", percent_it))
    print("{0:17}{1:>5.2f}".format("ICT Students", percent_ict))
