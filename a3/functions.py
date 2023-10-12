# Developer: Anthony Patregnani

# Course: LIS4969, Exploration into AI, Machine and Deep Learning

# Semester: Fall 2023


def get_requirements():

    print("\nProgram Requirements:\n"
          + "1. Calculate Home Interior Paint Cost. \n"
          + "2. Must Use Float Data Types.\n"
          + "3. Must Use SQFT_PER_GALLON constant (350).\n"
          + "4. Must Use Iteration Structure. \n"
          + "5. Format, right align numbers, and round to two decimal places.\n"
          + "6. Create at least five functions that are called by the program.\n"
                + "a. main()\n"
                + "b. get_requirements().\n"
                + "c. estimate_painting_cost()\n"
                + "d. print_painting_cost()\n"
                + "e. print_painting_percentage()\n")

def estimate_painting_cost():

    answer = 'y'

    while answer == 'y':

        SQFT_PER_GALLON = 350
        numGallons = 0

        print("Input:")
        inter_sqft = float(input('Enter total SQFT: '))
        price_per_gallon = float(input('Enter price per gallon: '))
        paint_rate = float(input('Enter hourly painting rate: '))


        numGallons = inter_sqft / SQFT_PER_GALLON

        paint_cost = price_per_gallon * numGallons
        labor_cost = paint_rate * inter_sqft
        total_cost = paint_cost + labor_cost

        paint_percent = (paint_cost / total_cost) * 100
        labor_percent = (labor_cost / total_cost) * 100
        total_percent = (total_cost / total_cost) * 100

        print_painting_estimate(inter_sqft, SQFT_PER_GALLON, numGallons, price_per_gallon, paint_rate)
        print()
        print_painting_percentage(paint_cost, labor_cost, total_cost, paint_percent, labor_percent, total_percent)
        print()


        answer = input("Estimate another paint job? (y/n): ")

        while answer == 'n':
            print("Thank you for using our Paint Estimator.")
            print("Please see our website: https://www.anthonypatregnani.tech")
            break


def print_painting_estimate(inter_sqft, SQFT_PER_GALLON, numGallons, price_per_gallon, paint_rate):
    print("\nOutput:")
    print("{0:<20} {1}".format('Item', 'Amount'))
    print("{0:<20} {1:,.2f}".format('Total SQFT:', inter_sqft))
    print("{0:<20} {1:,.2f}".format('SQFT per Gallon:', SQFT_PER_GALLON))
    print("{0:<20} {1:,.2f}".format('Number of gallons:', numGallons))
    print("{0:<20} ${1:,.2f}".format('Paint per gallons:', price_per_gallon))
    print("{0:<20} ${1:,.2f}".format('Labor per sqft:', paint_rate))
    

def print_painting_percentage(paint_cost, labor_cost, total_cost, paint_percent, labor_percent, total_percent):
    print("{0:<10} {1:<15} {2}".format('Cost', 'Amount', 'Percent'))
    print("{0:<10} ${1:<15,.2f} {2:,.2f}".format('Paint:', paint_cost, paint_percent))
    print("{0:<10} ${1:<15,.2f} {2:,.2f}".format('Labor:', labor_cost, labor_percent))
    print("{0:<10} ${1:<15,.2f} {2:,.2f}".format('Total:', total_cost, total_percent))
