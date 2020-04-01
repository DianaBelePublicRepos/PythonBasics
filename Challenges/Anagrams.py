#Check if a string is an anagram or not - use sorted to sort the string, then compare

def check(s1, s2):
    # The sorted strings are checked
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

    # Driver code
s1 = "listen"
s2 = "silent"
check(s1, s2)