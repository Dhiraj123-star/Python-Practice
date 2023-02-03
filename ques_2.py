# python code to remove vowels from the string
str = input("Enter a string: ")
result = ' '
for i in str:
    if i  in ('a','e','i','o','u'):
        i=''
    result +=i
print(result)