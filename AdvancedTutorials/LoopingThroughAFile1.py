with open('quotes.txt') as f:
    #Reads in all lines first, then loops through
    for one_line in f.readlines():
        print(one_line)

print("-" * 15)

#Using enumerate()
with open('quotes.txt') as f:
    #If counter is even number, print with no extra newline
    for one_line in enumerate(f.readlines()):
        #one_line[0] contains the number of the line
        if one_line[0] % 2 == 0:
            print(one_line[1], end='')
    #Otherwise print a couple spaces and an extra newline
    else:
        print(' ' + one_line[1])
