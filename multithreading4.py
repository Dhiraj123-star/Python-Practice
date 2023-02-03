# threading.timer()
# this function is used to create a new thread and specify
# the time after which it should start.
# once it starts , it should call the specified function

import threading

def delayed():
    print("Print after 3 seconds")

thread = threading.Timer(3,delayed)
thread.start()
