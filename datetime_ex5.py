# timezone represents the standard time which depends upon
# which part of the world is considered

import datetime
import pytz

localtime = datetime.datetime.now()
print('local time: ',localtime)

utctime = datetime.datetime.now(pytz.utc)
print('UTC time zone: ',utctime)

ustime = datetime.datetime.now(pytz.timezone('US/CENTRAL'))
print('US time zone: ',ustime)