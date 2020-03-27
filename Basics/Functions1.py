def hello(): #Practice function
    ''' A docstring describing a function'''
    print("Hello")

hello()

def hello_multi_params(fname, lname, datestring=''): #Practice function
    ''' A docstring describing the function '''
    msg = "Howdy " + fname + " " + lname
    if len(datestring) > 0:
        msg += " you mentioned " + datestring
    print(msg)

hello_multi_params('Alan', 'Simpson', '12/31/2019')
hello_multi_params("Miki", "KittyCat")

def alphabetize(original_list=[]): #Function for sorting in alphabetical order
    '''Pass any list in square brackets, displays a string with items sorted'''
    # Inside the function make a working copy of the list passed in
    sorted_list = original_list.copy()
    # Sort the working copy
    sorted_list.sort()
    # Make a new empty string for output
    final_list = ''
    # Loop through sorted list and append name and command and space
    for name in sorted_list:
        final_list += name + ','
    #Knack of last comma space if final list is long enough
    final_list = final_list[:-2]
    #Print the alphateized list
    print(final_list)

names_of_felines = ['Muttens', "Schroedinger", "Athena", "Aphaea", "Nyx"]
alphabetize(names_of_felines)

#Passing in any number of arguments with *args

def sorter(*args):
    newlist = list(args)
    newlist.sort()
    print(newlist)

sorter(1, 0, 0.555, 33, 987654567, 22443243.0989889)