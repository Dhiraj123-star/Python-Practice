# time in datetime module
import datetime

time1 = datetime.time()

print("without passing any attribute: ",time1)

time2 = datetime.time(hour=12,minute=34,second=56)
print("By passing hour,minute and second attributes: ",time2)

time1 = time1.replace(hour=17)
print('by replacing the hour attribute in time1 : ',time1)

time2 = time1.replace(minute=20)
print('by replacing the minute attribute in time2 ',time2)
