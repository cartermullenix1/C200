import os

def getCurrentDirectory():
    """
    This uses a command built into the python module `os` 
    that shows the current working directory. 

    Returns:
        A string that shows the current working directory 
        (Where the program is being executed at)
    """
    return os.getcwd()




def readingEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab7/blank.txt","r") as f_in:
        lines  = f_in.readlines()
        for line in lines:
            print("Here is line: " + line)
            
    return lines
            


def readingEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    raw_string = r'Laboratory/Lab7/blank.txt'
    escaped_strings = 'Laboratory//Lab7//blank.txt'
    with open("Laboratory/Lab7/blank.txt","r") as f_in:
        lines  = f_in.readlines()
        
    return lines


def writeEx1():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    a = ["a","b","c", "d", "e", "f"]
    with open("Laboratory/Lab7/wrong.txt","w") as f_out:
        for letter in a:
            f_out.write(letter + "\n")
            


def writeEx2():
    """
    This function will not return anything. 

    This function will be a "workspace" for us to practice reading files
    """
    with open("Laboratory/Lab7/wrong.txt","a") as f_app:
        for _ in range(4):
            f_app.write("More text!\n")



def FileIO_example(filePath, newFile): 
    '''
    Given a file path, we want to open the file, read each line and count
    the number of vocabs in each line. We will write to
    the newFile the lines that have more than 5 vocabs and clean them up
    (use strip). You are provided the path to the file we want to write.

    Return number of all lines that has less than or equal to 5 vocabs.
    '''
    with open(filePath, "r") as f_in, open(newFile,"w") as f_out:
        counter = 0
        lines = f_in.readlines()
        for line in lines:
            words = line.strip().split()

            size = len(words)
            
            if size > 5:
                f_out.write(line.strip() + "\n")
            
            else:
                counter += 1
    return counter


def calculation(filePath):
    '''
    Given a file path, we want to open the file, read each line. in each line we have a number
    we want to calculate the summation of numbers in last 2 lines and write the sum at the end of the 
    file we read from it. (eah time that we run this function we add one number of fibonacci series to the file)
    '''
    with open(filePath, "r") as f_in:
        lines = f_in.readlines()
        second_to_last_elem = lines[-2].strip()
        last_elem = lines[-1].strip()
    
    with open(filePath, "a") as f_app:
        number = int(second_to_last_elem) + int(last_elem)
        f_app.write(str(number) + '\n')


if __name__ == "__main__":
    print()
    print("Examples of Reading")
    print("Our current working directory: " + getCurrentDirectory())
    print()
    print("Reading")
    readex1 = readingEx1()
    print("~"*30)
    print(readex1, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    
    readex2 = readingEx2()
    print("~"*30)
    print(readex2, end="") # end= removes the \n automatically added
    print("*EOF*")
    print("-" * 20)
    print()

    print("Writing")
    print("-" * 20)
    writeEx1()
    writeEx2()
    print()
    print("Strip Lab Result: " + str(FileIO_example("Laboratory/Lab7/testing.data", "Laboratory/Lab7/clean.txt")))

    calculation("Laboratory/Lab7/calculation.txt")