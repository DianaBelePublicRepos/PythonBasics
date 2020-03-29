with open('quotes.txt') as f:
#Read in entire file
    content = f.read()
    print(content)

#Separating exercises with dashes
print("-" * 15)

with open('quotes.txt') as f:
    content = f.readlines()
    print(content)

print("-" * 15)

with open('quotes.txt') as f:
    content = f.readline()
    print(content)