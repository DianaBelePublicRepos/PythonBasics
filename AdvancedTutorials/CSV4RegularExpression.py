import csv
import datetime as dt
from re import sub

#Open the CSV file with a UTF-8 encoding, don't read in newline characters
with open('sample.csv', encoding='utf-8', newline='') as f:
    # #Create a csv row counter and a row reader
    reader = enumerate(csv.reader(f))
    #Loop through one row at a time, i is counter, row is entire row
    for i, row in reader:
        #Row 0 is just column headings, ignore it:
        if i > 0:
            #Whole name split into two at comma.
            try:
                full_name = row[0].split(',')
                #Last name, strip extra spaces
                last_name = full_name[0].strip()
                #First Name, strip extra spaces
                first_name = full_name[1].strip()
                #Birth year
                birth_year = int(row[1] or 0)
            except IndexError:
                full_name = last_name = first_name = ""
            #Birth year integer, zero for empty string.
            birth_year = int(row[1] or 0)
            #Date joined is a date
            try:
                date_joined = dt.datetime.strptime(row[2], "%m/%d/%Y").date()
            except ValueError:
                date_joined = None
            #Is_active is a Boolean, automatically False for empty string
            is_active = bool(row[3])
            #Remove $, commas, leading and trailing spaces
            str_balance = (sub(r'[\s\$,]','',row[4])).strip()
            #Balance is a float or zero for empty string
            balance = float(str_balance or 0)
            print(first_name, last_name, birth_year, date_joined, is_active, balance)
print("Done!")