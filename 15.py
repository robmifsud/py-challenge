from datetime import datetime, timedelta
from calendar import isleap
  
# Create Custom Function
def date_range(start, end):
    delta = end - start
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days
  
startDate = datetime(1582, 10, 15)
endDate = datetime(2023, 8, 15)
      
datesRange = date_range(startDate, endDate)
ls = []
for date in datesRange:
    if date.month == 1 and date.day == 26 and date.weekday() == 0 and isleap(date.year):
        ls.append((date.year, date.month, date.day, date.weekday()))

print(ls)

# from returned dates match with regex: 1\d+6
# 27th jan 1756: mozart's birthday
