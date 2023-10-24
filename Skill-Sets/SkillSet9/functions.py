def get_requirements():
    print("Python Looping Structures")
    print("\nProgram Requirements:\n"
          + "1. Print while loop.\n"
          + "2. Print for loops using range() function, and implicit and explicit lists.\n"
          + "3. Use break and continue statements.\n"
          + "4. Replicate display below.\n"
    )

def using_sets():
    
    print("\nInput: Hard coded-no user input")
    print()
    my_set = {1,3.14,2.0,'four','Five'}
    print("Print my_set created using curly brackets.\n")
    print(my_set)

    print("\nPrint type of my_set:")
    print(type(my_set))

    print()

    my_set1 = set([1,3.14,2.0,'four','Five'])
    print("\nPrint my_set1 created using set() functions with list:\n")
    print(my_set1)

    print()

    print("\nPrint type of my_set1:")
    print(type(my_set1))

    print()

    my_set2 = set((1,3.14,2.0,'four','Five'))
    print("\nPrint my_set2 created using set() functions with tuples:\n")
    print(my_set2)

    print()

    print("\nPrint type of my_set2:")
    print(type(my_set2))

    print()

    print("\nLength of my_set:")
    print(len(my_set))
    print()

    print("\nDiscard 'four':")
    my_set.discard('four')
    print(my_set)

    print()

    print("\nRemove 'Five':")
    my_set.remove('Five')
    print(my_set)

    print()

    print("\nLength of my_set:")
    print(len(my_set))

    print()

    print("\nAdd element to set(4) using add() method:")
    my_set.add(4)
    print(my_set)

    print()

    print("\nPrint length of my_set:")
    print(len(my_set))

    print()

    print("\nDisplay minimum number:")
    print(min(my_set))

    print()

    print("\nDisplay maximum number:")
    print(max(my_set))

    print()

    print("\nDisplay sum of numbers:")
    print(sum(my_set))

    print()

    print("\nDelete all set elements:")
    my_set.clear()
    print(my_set)

    print()

    print("\nLength of my_set:")
    print(len(my_set))

    