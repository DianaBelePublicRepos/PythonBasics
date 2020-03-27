
#Problem definition: rotate matrix from:
#
#1 2 3
#4 5 6
#7 8 9
#
#To 
#
#7 4 1
#8 5 2
#9 6 3


collector_appended = []

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        collector_appended.append(a[j][i])


sliced_list1 = collector_appended[:3]
sliced_list1.reverse()

sliced_list2 = collector_appended[3:6]
sliced_list2.reverse()

sliced_list3 = collector_appended[6:]
sliced_list3.reverse()

aggregated_list = [sliced_list1, sliced_list2, sliced_list3]


print (*aggregated_list, sep = "\n")


