# Calculating trailing zeros in the factorial of the number

def factorial_trailing_zeros(num):
    fact=num
    while num>1:
        fact*=num-1
        num-=1
    result=0

    for i in str(fact)[::-1]:
        if i=="0":
            result+=1
        else: break # when there is other zero except trailing zero
    return result

# driver code

num= int(input("Enter your number to count the trailing zero in factorial: "))
print("The trailing zero is/are: ", factorial_trailing_zeros(num)) 






    
