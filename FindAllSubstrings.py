

#Problem definition: Get all substrings of a string, sort them alphabetically
#then display the last item of the list

from itertools import combinations 

initial_string = "diana"
str(initial_string)

collector = [ initial_string[i: j] for i in range(len(initial_string))
				for j in range(i + 1, len(initial_string) + 1)]
collector.sort()

print(collector[-1])	
	
combine = [initial_string[x:y] for x, y in combinations( 
            range(len(initial_string) + 1), r = 2)] 

combine.sort()

print(combine[-1])	
