#  program that generate a fibonacci series in python

n=int(input("Enter the number of terms: "))
first=0 # first element of the series
second=1 # second element of the series
series=[first,second]

if n==0: 
    print("The required fibnacci series is: ",first)

else:
    for  i in range(0,n-2):
        num = series[i]+series[i+1]
        series.append(num)

    print(series)
