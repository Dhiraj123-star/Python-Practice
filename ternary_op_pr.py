# ternary operator program in Python
score =int(input("Enter your marks: "))
if score <70:
    if score<50:
        print("Fail")
    else:
        print("Merit")
else:
    print("Destination")

print("using nested ternary operator: ",end=" ")
print("Fail" if score<50 else "Merit" if score<70 else"Destination")
 