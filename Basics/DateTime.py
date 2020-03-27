import datetime as dt
today = dt.date.today()
#Store a date in a variable called last_of_teens
last_of_teens = dt.date(2019,12,30)
print(today, last_of_teens)
print(last_of_teens.month)
print(last_of_teens.day)
print(last_of_teens.year)
print(f"{last_of_teens:%A, %B %d, %Y}")
todays_date = f"{today:%m/%d/%Y}"
print(todays_date)
todays_date2 = f"{today:%x}"
print(todays_date2)
todays_date3 = f"{today:%A %B %d is day number %j of %Y}"
print(todays_date3)

midnight = dt.time()
print(midnight)
almost_midnight = dt.time(23,59,59,999999)
print(almost_midnight)
right_now = dt.datetime.now()
print(right_now)

