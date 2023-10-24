def get_requirements():
    print("Python Tuples ")
    print("\nProgram Requirements:\n"
          + "1. Tuples (Python Data structure): *immutable* (cannot be changed!), ordered by sequence of elements.\n"
          + "2. Tuples are immutable/unchangeable--that is, cannot insert, update, delete.\n"
          + "3. Create tuple using parentheses (tuple): my_tuple1 = (\"cherries\", \"apples\", \"bananas\", \"oranges\") \n"
          + "4. Create tuple (packing), that is, *without* using parentheses (aka tuple \"packing\"): my_tuple2 = 1,2,\"three\", \"four\"\n"
          + "5. Python tuple (unpacking), that is, assign values from tuple to sequence of variables: fruit1, fruit2, fruit3, fruit4 = my_tuple1"
          + "6. Create a program that mirrors the following IPO format")
    

def using_tuples():
    print("\nInput: Hard coded-no user input")

    my_tuple1 = ("cherries", "apples", "bananas", "oranges")

    my_tuple2 = 1,2, "three", "four"

    print("\nOutput:")
    print("Print my_tuple1:")
    print(my_tuple1)

    print()

    print("Print my_tuple2:")
    print(my_tuple2)

    print()

    fruit1, fruit2, fruit3, fruit4 = my_tuple1
    print("Print my_tuple1 unpacking:")
    print(fruit1, fruit2, fruit3, fruit4)

    print()

    print("Print third element in my_tuple2:")
    print(my_tuple2[2])

    print()

    print("Print \"slice\" of my_tuple1 (second and fourth elements):")
    print(my_tuple1[1:3])

    print()

    print("Reassign my_tuple2 using parentheses.")
    my_tuple2 = (1,2,3,4)
    print("Print my_tuple2:")
    print(my_tuple2)

    print()

    print("Reassign my_tuple2 using \"packing\" method(no parentheses.)")
    my_tuple2 = 5,6,7,8
    print("Print my_tuple2:")
    print(my_tuple2)

    print()

    print("Print number of elements in my_tuple1:" + str(len(my_tuple1)))

    print()
    print("Print type of my_tuple1:" + str(type(my_tuple1)))

    print()

    print("Delete my_tuple1: \nNote: will generate error if trying to print after no longer exists.")
    del my_tuple1