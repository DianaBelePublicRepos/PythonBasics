people = {
    'htanaka' : 'Haru Tanaka',
    'ppatel' : 'Priya Patel',
    'bagarcia' : 'Benjamin Alberto Garcia',
    'zmin' : 'Zhang Min',
    'afarooqi' : 'Ayesha Farooqi',
    'hajackson' : 'Hanna Jackson',
    'papatel' : 'Pratyush Aarav Patel',
    'hrjackson' : 'Henry Jackson'
}

print(people)
print(people['papatel'])


#Getting the value for the key from the dictionary
person = 'zmin'
print(people[person])

#Length of a dictionary
howmanypeople = len(people)
print(howmanypeople)

#Seeing if a key exists in the dictionary
print('hajackson' in people)
print ('schmeedledorp' in people)

#With get() the program doesn't crash when the key doesn't exist in the dictionary
nodude = 'schmeedledorp'
print(people.get(nodude))
#Same thing with a custom message when the key is not found in the dictionary
print(people.get(nodude, 'Batman!!Batman!!!'))

#Changing the value of a key
people['hajackson'] = "Hannah Jackson-Smmmmmmmmmmm"
print(people['hajackson'])

#Adding a new element to the dictionary using update() or update a current one
people.update({'hajackson': 'Hahaha'})
people.update({'wwigings' : 'Wanda Wiggings'})
print(people)

#Looping through the dictionary and displaying it
for person in people:
    print(person + " = " + people[person])

#Print keys
for person in people:
    print(person)

#Print dictonary values only
for person in people:
    print(people[person])

#Using items after the dictionary referenced in the for loop
for key, value in people.items():
    print(key, "=", value)

#Copy a dictionary
mates = people.copy()
print(mates)
#Pop also available for dictionaries
mates.pop('zmin')
print(mates)
#Popitem removes the last item in the dictionary
mates.popitem()
print(mates)