# timedelta helps to find the difference between the 2 dates/time which 
# is provided by the datetime.timedelta class

import datetime

date1 = datetime.timedelta(days=1,hours=23,minutes=40)
print('date1: ',date1)

date2 = datetime.timedelta(days=5,hours=23,minutes=40)
print('date2: ',date2)

difference = date2-date1

print('difference between date2 and date1 is: ',difference)
