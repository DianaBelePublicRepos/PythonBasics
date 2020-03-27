#Tuples are immutable lists - after you define it you can't change it
#Syntax is using "()" instead of [] like for lists

#Get the length of a Tuple
prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))

#Count
print(prices.count(9.98))

#Verify for existence of smth in tuple
print(4.95 in prices)

#Looping through a tuple
for price in prices:
    print(price)
    print(f"${price:.2f}")

