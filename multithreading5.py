# synchronisation using lock
# the lock helps us the synchronisation of two or more threads 
# it has two methods (acquire() and release())
# acquire() method is used to acquire the lock
# release () is used to release the acquired lock

import threading
# declaring the lock 
lock = threading.Lock()
deposit =500
def add_profit(): # function to add profit to the deposit 
    global deposit
    for _ in range(100):
        lock.acquire()
        deposit = deposit+10
        lock.release()
def pay_bill(): # function to deduct money from the deposit 
    global deposit 
    for  _ in range(100):
        lock.acquire()
        deposit=deposit-10
        lock.release()

# creating threads

thread1 = threading.Thread(target=add_profit,args=())
thread2 = threading.Thread(target=pay_bill,args=())

# starting threads
thread1.start()
thread2.start()

# waiting for both the threads to finish executing
thread1.join()
thread2.join()

print(deposit) # displaying the final value of the deposit 