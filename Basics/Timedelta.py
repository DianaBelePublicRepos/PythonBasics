import datetime as dt

new_year_day = dt.date(2019,1,1)
memorial_day = dt.date(2019,5,27)
days_between = memorial_day - new_year_day

print("The number of days in between our 2 original dates is", days_between)

#birthday special
dis_birthday = dt.date(1985,9,21)
today = dt.date.today()
delta_age = today - dis_birthday
print("Diana is this numbers of days old:", delta_age)
days_old = delta_age.days
years_old = days_old // 365
months = (days_old % 365) // 30
print (f"You are {years_old} years old and {months} months.")

