s = "Abracadabra Hocus Pocus you're a turtle dove"
print("Is there a lower case letter t contained in s?")
print("t" in s)
print("Is there an uppercase letter t contained in s?")
print("T" in s)
print("Is there no T in s?")
print("T" not in s)
print("Print 15 - in a row")
print("-" * 15)
print("Print first character in string X")
print(s[0])
print("Print characters 33 - 39 from string x")
print(s[33:39])
print("Print every third character in s starting at zero")
print(s[0:44:3])
print("Print lowest character in s (a space is lower char than a)")
print(min(s))
print("Print highest char in s")
print(max(s))
print("Where is the first uppercase P?")
print(s.index("P"))
print("Where is the first lowercase o in the latter half of the string s - starts counting at 0")
print(s.index("o",22,44))
print("How many lowercase letter a in string s")
print(s.count("a"))


