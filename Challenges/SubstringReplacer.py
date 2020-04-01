#Builtin method in python
#replace() is an inbuilt function in Python programming language that returns a copy of the string
# where all occurrences of a substring is replaced with another substring.

#string.replace(old, new, count)

string = "gummy bears for geeks have stardust shape"

# Prints the string by replacing geeks by Geeks
print(string.replace(" ", "%20"))

# Prints the string by replacing only 3 occurrence of Geeks
print(string.replace(" ", "%20", 3))