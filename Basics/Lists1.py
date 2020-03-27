students = ["Mark","Amber","Todd","Anita","Sandy"]
print(students[0])

#Looping through lists
for x in students:
    print(x)

print("Checking for items in a list")
has_anita = "Anita" in students
print("Is Anita there? " + str(has_anita))

has_bob = "Bob" in students
print("Is Bob anywhere in there? " + str(has_bob))

print(len(students))

#adding to the end of a list
students.append("Gooper")
print(students)

student_name = "Amanda"

#Add student_name if not already in the list
if student_name in students:
    print(student_name + " is already in the list")
else:
    students.append(student_name)
    print(student_name + " added to the list")

#Inserting an item in a list
new_guy = "Samantha"
students.insert(0,new_guy)
print(students)

#Assignment of item in a list
students[3] = "Hobart"
print(students)

#Combining lists
list1 = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
list2 = ["Huey", "Dewey", "Louie", "Nader", "Bubba", "Louie", "Louie", "Nader"]

list1.extend(list2)
print(list1)

while "Louie" in list1:
    list1.remove("Louie")
print(list1)


#Looping through a list to remove multiple occurences
letters = ["A", "B", "C", "D", "E", "F", "G"]
#Remove the first item
first_item = letters.pop(0)
#Remove the last item
last_item = letters.pop()

print("Things that were removed: " + first_item + " + "+  last_item)

#Clearing all items from a list
letters.clear()
print(letters)
#Counting the number of occurences
number_of_Naders = list1.count("Nader")
print(number_of_Naders)


