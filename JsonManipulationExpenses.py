import json

#Excel data 
filename = 'expenses.json'

#Open the file 
with open(filename, 'r') as f:
	# Load the whole json file into an object named people
	people = json.load(f)

print (people)
print(type(people))

#Display everything that's in the p variable
for p in people:
	print(type(p))

for p in people:
	print (p)
