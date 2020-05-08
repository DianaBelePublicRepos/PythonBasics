import csv


"""
 The CSV file is opened as a text file with Python’s built-in open() function, 
 which returns a file object. 
"""

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

"""
Read CSV data directly into a dictionary

"""


with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Columnos los nameos are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} workie works in the {row["department"]} department, and was born in uuuu!  {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


