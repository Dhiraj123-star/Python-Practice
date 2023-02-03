import sys

randomList =['a',0,12]

for entry in randomList:
    try:
        print("The entry is: ",entry)
        r=1/int(entry)
        break
    except Exception as e:
        print("Oops!!",e.__class__,"occurred")
        print()

print("The reciprocal of",entry,"is",r)




