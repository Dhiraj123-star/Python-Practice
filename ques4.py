# decorator 
def decorator_lowercase(func):
    def wrapper():
        funct=func()
        input_lowercase = funct.lower()
        return input_lowercase
    return wrapper

@decorator_lowercase
def info():
    return "HELLO PYTHON"

print(info())