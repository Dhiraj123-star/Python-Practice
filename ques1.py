# count the occurence of given character in the string 
str= input("Please enter a string: ")
chr = input("please enter a character: ")
count=0
for i in range(len(str)):
    if (str[i]==chr):
        count+=1

print(count)


