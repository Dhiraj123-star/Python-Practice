#reverse the number 

num = int(input("Enter your number :"))

reverse = 0

while (num>0):
    rev= num%10
    reverse = reverse*10+rev
    num=num//10

print("The reverse number is ",reverse)