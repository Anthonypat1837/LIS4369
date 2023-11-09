import random as r

def get_requirements():
    print("Pseudo-Random Number Generator")
    print("\nProgram Requirements:\n"
        + "1. Get user beginning and ending integer values, and store in two variables.\n"
        + "2. Display 10 pseudo-random numbers between, and including user input values.\n"
        + "3. Must use integer data types.\n"
        + "4. Example 1: Using range() and randint() functions.\n"
        + "5. Example 2: Using a list with range() and shuffle() functions.")

def random_number_generator():  

    print("\nInput:")
    beginput = int(input("Enter beginning value: "))
    endinput = int(input("Enter ending value: "))

    print("\nOutput:")
    print("\nExample 1: Using range() and randint() functions:")
    x = range(10)
    for i in x:
        print(r.randint(beginput, endinput), end=" ")

    print("\nExample 2: Using range() and shuffle() functions:")
    num_list = []
    for i in x:
        # rand_num = r.randint(beginput, endinput)
        num_list.append(i+1)
        r.shuffle(num_list)
    print(*num_list, end=" ")
