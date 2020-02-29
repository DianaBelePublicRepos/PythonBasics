# Script to display the Fibonacci sequence up to a certain number of selections

numberofselections = int(input("How many numbers do you want this computed for? "))

#Initial numbers 
n1, n2 = 0, 1 
counter = 0

#Checking if the number of terms is valid
if numberofselections <= 0:
	print ("Please enter a positive number in order to have a valid sequence :) ")
elif numberofselections == 1:
	print ("\n Fibonacci sequence up to\n ",numberofselections,":")
	print (n1)
else:
	print("\n Fibonacci sequence up to\n", numberofselections,":")
	while counter < numberofselections:
		print(n1)
		nth = n1 + n2 
		#Update the values to the next ones in the sequence
		n1 = n2
		n2 = nth
		counter += 1 
		