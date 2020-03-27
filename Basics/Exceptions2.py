class Error(Exception):
    ''' Base class for other exceptions'''
    pass

#Defining own exceptions as subclass of Error

class EmptyFileError(Error):
    pass

try:
    #Open the file (no error checks here)
    thefile = open('people.csv')
    #Count the number of lines
    line_count = len(thefile.readline())
    #If there are fewer than 2 lines raise an exception
    if line_count < 2:
        raise EmptyFileError

except FileNotFoundError:
        print("\nThere is no people.csv file here")

#Handles my custom error for too few rows
except EmptyFileError:
        print("\nYour people.csv file doesn't have enough stuff.")

except Exception as e:
        # Show the error
        print("\n\nFailed: the error was " + str(e))
        # Close the file
        thefile.close()
else:
    #This code runs only if there aren't any exceptions
    print()

    #File must be opened
    for one_line in thefile:
        print(one_line)
    thefile.close()
    print("Success")