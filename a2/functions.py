def get_requirements():
    print("Payroll Calculator")
    print("\nProgram Requirements:\n"
          + "1. Must use float data type for user input.\n"
          + "2. Overtime rate: 1.5 times hourly rate (hours over 40).\n"
          + "3. Holiday rate: 2.0 times hourly rate (all holiday hours).\n"
          + "4. Must format currency with dollar sign, and round to two decimal places. \n"
          + "5. Create at least three functions that are called by the program:\n"
          + "\ta. main(): calls at least two other functions.\n"
          + "\tb. get_requirements(): displays the program requirements.\n"
          + "\tc. calculate_payroll(): calculates an individual one-week paycheck.\n")
    
def calculate_payroll():
    base_hours = 40
    ot_rate = 1.5
    holiday_rate = 2.0

    print("Input:")
    hours = float(input('Enter hours worked: '))
    holiday_hours = float(input('Enter holiday hours: '))
    pay_rate = float(input('Enter hourly pay rate: '))

    base_pay = base_hours * pay_rate
    overtime_hours = hours - base_hours

    if hours > base_hours:

        # calculate and display overtime pay
        overtime_pay = overtime_hours * pay_rate * ot_rate

        # calculate and display holiday pay
        holiday_pay = holiday_hours * pay_rate * holiday_rate
        # calculate gross pay
        gross_pay = base_hours * pay_rate + overtime_pay + holiday_pay

        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)


    else:
        overtime_pay = 0
        holiday_pay = holiday_hours * pay_rate * holiday_rate
        gross_pay = hours * pay_rate + holiday_pay
        
        print_pay(base_pay, overtime_pay, holiday_pay, gross_pay)



    print()

def print_pay(base_pay, overtime_pay, holiday_pay, gross_pay):
    print("\nOutput:")
    print("{0:<10} ${1:,.2f}".format('Base:', base_pay))
    print("{0:<10} ${1:,.2f}".format('Overtime:', overtime_pay))
    print("{0:<10} ${1:,.2f}".format('Holiday:', holiday_pay))
    print("{0:<10} ${1:,.2f}".format('Gross:', gross_pay))
