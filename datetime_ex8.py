# strftime() module 
import datetime

todaydatetime= datetime.datetime.now()

print('Current date and time: ',todaydatetime)
print('fetched out year from current date: ',todaydatetime.strftime('%Y'))
print('fetched out month from current date: ',todaydatetime.strftime('%B'))
print('fetched out day from current date: ',todaydatetime.strftime('%A'))
print('formatted the time from above generated date time: ',todaydatetime.strftime('%H%M%S'))
