# count the total number of words 

def count_words(sentence):
    words = sentence.split()
    return len(words)

# call the function

input_words = input("Enter your sentence : ")

print("total number of words : ",count_words(input_words))