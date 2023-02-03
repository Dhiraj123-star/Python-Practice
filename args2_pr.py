# **kwargs in Python
def makeSentence(**words):
    sentence=" "
    for word in words.values():
        sentence+=word
    return sentence

print("Sentence: ",makeSentence(a='Kwargs',b=' are',c=' awesome'))
