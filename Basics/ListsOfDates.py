import datetime as dt

datelist = []

datelist.append(dt.date(2020,12,31))
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))

datelist.sort()
for date in datelist:
    print(f"{date:%m/%d/%Y}")

