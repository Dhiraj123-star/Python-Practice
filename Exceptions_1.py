# import sys to get the exception information
import sys

randomList=['b',0,3]

for entry in randomList:
    try:
        print("The entry is: ",entry)
        r=1/int(entry)
        break
    except:
        print("Oops!!",sys.exc_info()[0],"occurred")
        print("next entry")
        print()

print("The reciprocal of",entry,"is",r)
