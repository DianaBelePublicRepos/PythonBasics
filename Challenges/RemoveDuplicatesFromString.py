from collections import OrderedDict

# Function to remove all duplicates from string
# and order does not matter
def removeDupWithoutOrder(input_string):

	# set() --> A Set is an unordered collection
	#		 data type that is iterable, mutable,
	#		 and has no duplicate elements.
	# "".join() --> It joins two adjacent elements in
	#			 iterable with any symbol defined in
	#			 "" ( double quotes ) and returns a
	#			 single string
	return "".join(set(input_string))

# Function to remove all duplicates from string
# and keep the order of characters in the same manner
def removeDupWithOrder(input_string):
	return "".join(OrderedDict.fromkeys(input_string))

# Driver program
if __name__ == "__main__":
	str = "abracadabra"
	print ("Without Order = " + removeDupWithoutOrder(str))
	print ("With Order = " + removeDupWithOrder(str))
