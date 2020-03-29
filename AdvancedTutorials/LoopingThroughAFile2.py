with open('quotes.txt') as f:
    one_line = f.readline()
    while one_line:
        print(one_line, end='')
        one_line = f.readline()
print(' ')
print("-" * 15)

#Store a number to use asa loop counter
counter = 1
#Open the file
with open('quotes.txt') as f:
    #Read one line from a file
    one_line = f.readline()
    #As long as there are lines to read
    while one_line:
        #If the counter is an even number, print a couple of spaces
        if counter % 2 == 0:
            print(' ' + one_line)
        #Otherwise print with no newline at the end
        else:
            print(one_line,end='')
        #Increment the counter
        counter += 1
        #Read the next line
        one_line = f.readline()
