# palindrome number in Python

def is_palindrome(string):
    string =string.lower().replace(" ","") # convert the string into lowercase and replace the space 
    reversed_str = string[::-1] # reverse 
    return string == reversed_str


# test the function

str1 = "racecar"
str2 = "python"

print("Palindrome : ",is_palindrome(str1))
print("Palindrome: ",is_palindrome(str2))