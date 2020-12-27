"""""
Code by: Charanpreet Singh
Email: Charanmakkar@gmail.com
Linkedin profile: https://www.linkedin.com/in/charanpreet-singh-a29949133/
DM linkedin if need any help (Always open to help)
Development date Aug 19, 2020
Final editing done on Aug 25, 2020
Github Upload: Dec 27, 2020
"""""

##Importing required libraries
from ctypes import *


""""
Functions and parameteres start from here.
all the defined libraries are defined above this note.
"""
####Function to set parameters for communicattion
def convert(decimal_value):
    value = str(decimal_value)
    #print(value)
    #print(type(value))
    value = hex(int(value))
    #print("Hex = " + str(value))
    value = str(value)
    value = value[2:]
    #print(value)
    value = value + '0000'

    def convert(s):
        i = int(s, 16)                   # convert from hex to a Python int
        cp = pointer(c_int(i))           # make this into a c integer
        fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
        return fp.contents.value
    
    finalValue = str(convert(value))
    return finalValue

value = convert(2020)
print(value)
