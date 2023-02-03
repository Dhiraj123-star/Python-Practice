# python threading function
# threading.active_count()
import threading
import time
from threading import Thread

def sleepme(x):
    print("Thread %x going to sleep for 2 seconds " %x)
    time.sleep(2)
    print("Thread %x is active now."%x)

for x in range(1,10):
    th= Thread(target=sleepme,args=(x, ))
    th.start()
    print("Current Thread count: %x" %threading.active_count())
