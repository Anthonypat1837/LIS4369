import os

lincoln_address = '''
President Abraham Lincoln\'s Gettysburg Address:
Fourscore and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, 
and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, 
can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place 
for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we can not dedicate-we can not consecrate-we can not hallow-this ground. 
The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. 
The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. 
It is rather for us to be here dedicated to the great task remaining before us-that from these honored dead we take increased devotion to that 
cause for which they gave the last full measure of devotion-that we here highly resolve that these dead shall not have died in vain-that this 
nation, under God, shall have a new birth of freedom-and that government of the people, by the people, 
for the people shall not perish from the earth.

Abraham Lincoln
November 19, 1863
'''

def get_requirements():
    print("File Write and Read\n")
    print("\nProgram Requirements:\n"
          + "\n1. Create write_read_file subdirectory with two files: main.py and functions.py."
          + "\n2. Use President Lincoln's Gettysburg Address: Full Text."
          + "\n3. Write address to file."
          + "\n4. Read address from same file."
          + "\n5. Create Python Docstrings for functions in functions.py file."
          + "\n6. Display Python docstrings for each function in functions.py file."
          + "\n7. Display full file path."
          + "\n8. Replicate display below.")
    
def file_write():
    '''Usage: creates file, and writes contents of global variable to file
    Parameters: none
    Returns: none
    '''
    with open('test.txt', 'w') as writer:
        for line in lincoln_address:
            writer.write(line)

    writer.close()

def file_read():
    '''Usage: reads content of written file
    Parameters: none
    Returns: none
    '''
    with open('test.txt', 'r') as reader:
        for line in reader:
            print(line, end='')
    
    print("\nFull file path:")
    print(os.getcwd() + '\\' + reader.name)
    reader.close()

def write_read_file():
    '''Usage: Calls two functions:
    \t1. file_write() # writes to file
    \t2. file_read() # reads from file
    Parameters: none
    Returns: none
    '''
    help(write_read_file)
    help(file_write)
    help(file_read)

    file_write()
    file_read()


    

