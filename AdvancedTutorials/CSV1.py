import csv
#Open the CSV file with a UTF-8 encoding, don't read in newline characters
with open('sample.csv', encoding='utf-8', newline='') as f:
    # #Create a csv row counter and a row reader
    reader = enumerate(csv.reader(f))
    #Loop through one row at a time, i is counter, row is entire row
    for i, row in reader:
        print(i, row)
print("Done!")

#Output is going to be in this format:
# 0 ['Full Name', 'Birth Year', 'Date Joined', 'Is Active', 'Balance']
# 1 ['Angst, Annie', '1982', '1/11/2011', 'TRUE', '$300.00']
# 2 ['Bonanas, Garry', '1973', ' 2/11.2012', 'FALSE', '-$123', '45']
# 3 ['Schadenfreude, Sandy', '2004', '3/3/2003', 'TRUE', '$0.00']
# 4 ['Weltschmerz, Wanda', '1995', '4/24/1994', 'FALSE', '$999,999.99']
# 5 ['Malaise, Mindy', '2006', '5/5/2005', 'TRUE', '$454.01']
# 6 ["O'Possum, Ollie", '1987', '7/27/1997', 'FALSE', '-$1,000.00']
# 7 ['', '', '', '', '']
# 8 ['Pussilanimity, Pamela', '1979', '8/8/2008', 'TRUE', '12,345.67']
# Done!
