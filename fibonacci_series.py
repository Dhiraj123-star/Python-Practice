# fibonacci series in python

def fibonacci_series(n):
    a,b=0,1
    for i in range(n):
        a,b =b,a+b
        print(a)


# user input 

number = int(input("Enter your number:  "))

fibonacci_series(number)