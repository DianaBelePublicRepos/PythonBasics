#Items in sets have no specific order

sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}

#Length
print(len(sample_set))

#items in sets cannot be changed either
#Can add items to sets
sample_set.add(11.23)

#Adding items to sets with update - feeding a list to it
sample_set.update([88, 123.45, 2.98])

#Copy sets - because items are not in a specific order new items added to the set may not be in the same order
ss2 = sample_set.copy()
print(ss2)

print("\nLoop through the set and display each item formatted.")
for price in sample_set:
    print(f"{price:>6.2f}")