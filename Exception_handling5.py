# The raise statement allows the programmer to force a specific
# exception to occur.

try:
    raise NameError("Hi, this is NameError raised!!")
except NameError:
    print("An Exception Occurred!!")
    raise # To determine whether the exception was raised or not.
