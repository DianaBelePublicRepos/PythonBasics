#generating reverse of a string
def reverse(s):
	return s[::-1]

def isPalindrome(s):
	#Call the reverse function on the string
	rev = reverse(s)

	#Checking to see if both strings are equal or not 
	if(s == rev):
		return True
	return False 


#Driver code
s = "malayalam"
ans = isPalindrome(s)

print(ans)

if ans == 1:
	print("Yeeeeey!!!! We have a match")
else: 
	print("Nope nope nope")