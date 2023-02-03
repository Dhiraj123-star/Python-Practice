# packing and unpacking using *args in Python
carCompany= ["Audi","BMW","Lamborghini"]
print(*carCompany) # unpacking

# packing and unpacking using **kwargs in Python

techStackOne = {"React":"Fackbook","Angular":"Google",".NET":"Microsoft"}
techStackTwo = {".NET":"Microsoft"}
mergedStack = {**techStackOne,**techStackTwo} # unpacking

print(mergedStack)
