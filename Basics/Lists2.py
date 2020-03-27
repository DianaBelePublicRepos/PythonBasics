#Finding an item in a list based on index and display it
grades = ["C", "B", "A", "D", "C", "B", "C"]

#Decide what to look for
look_for = "F"

#See if the item is in the list
if look_for in grades:
    #If it's there gget and show index
    print(str(look_for) + " is at index" + str(grades.index(look_for)))
else:
    #If not in the list, don't even try to look for index number
    print(str(look_for) + " isn't in the list.")

#Alphabetize list
grades.sort()
print(grades)

#Numbers sort
numbers = [14, 0, 56, -4, 99, 56, 11.23]
numbers.sort()
print(numbers)

#Lists with strings in mixture of lower and upper case
names = ["Zara", "Lupe", "Hong", "alberto", "Jake", "tyler"]
names.sort()
print("Results of first sorting: "+ str(names))
names.sort(key=lambda s:s.lower())
print("Results of second sorting: "+ str(names))

#Reversing a list
names.reverse()
print(names)

#Copying a list
backward_list = names.copy()
backward_list.reverse()
print(backward_list)