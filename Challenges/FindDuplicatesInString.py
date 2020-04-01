#Given string s determine if string has any duplicate chars

from collections import Counter

guinea_pig_string = "abracadabra"
counter = 0


#The super naive implementation
for i in guinea_pig_string:

    if guinea_pig_string[0] == guinea_pig_string[counter]:
        print("Yeeey")
        break

    print(i + " This one doesn't match")
    counter = counter + 1
    print(counter)

#The intelligent one

def find_dup_char(input):
    #Creating a dict using counter which will have strings as key and frequency as values
    WC = Counter(input)
    j = -1

    #Finding the number of occurences of a char and get the index of it
    for i in WC.values():
        j = j+1
        if(i > 1):
            for key, value in WC.items():
                 print(key, "=", value)

#Driver program
if __name__ == "__main__":
    input = guinea_pig_string
    find_dup_char(input)