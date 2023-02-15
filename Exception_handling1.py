# exception handling in Python 

a=[1,4,5,19]

try:
    print("Second Element = %d"%(a[1]))

    # throw error since there are only 4 elements
    print("Fifth element = %d"%(a[4]))
except:
    print("An error occurred")
