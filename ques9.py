# check number is palindrome or not
def checkPalindrome(n):
    reverse=0
    while (n>0):
        digit = n%10
        reverse=reverse*10+digit
        n=n//10
    return reverse

n= int(input("Enter your number: "))
if (checkPalindrome(n)==n): print("Number is palindrome")
else: print("Number is not palindrome")

