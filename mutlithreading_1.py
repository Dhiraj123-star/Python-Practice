# multithreading in python
import threading 

def print_cube(num):
    print("Cube: {}".format(num*num*num))

def print_sqr(num):
    print("Square: {}".format(num*num))

if __name__=='__main__':
    # creating threading 
    t1=threading.Thread(target=print_cube,args=(20,))
    t2= threading.Thread(target=print_sqr,args=(10 ,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed 
    t2.join()
    
    # both threads completely executed 
    print("Done!!")
    