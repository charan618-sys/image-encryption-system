"""
    This module contains all the code for functions used for conversion from one type to another
    It has 6 modules which converts from one data-type to another. For example if you want to convert 
    an integer value say 9 to binary string then simply call the function like int_to_binary_string(9)
    ,this will return binary string so store this into a variable.
"""

## converts an integer value directly to a 8-bit binary sting
def int_to_binary_string(int_value):
    return '00000000'[len(bin(int_value)[2:]):]+bin(int_value)[2:]

## converts an integer value directly to a 8-bit binary array
def int_to_binary_list(int_value):
    return list('00000000'[len(bin(int_value)[2:]):]+bin(int_value)[2:])

## converts a 8-bit binary string value directly to a 8-bit binary array
def binary_string_to_binary_list(binary_string):
    return list(binary_string)

## converts a 8-bit binary array directly to a 8-bit binary sting
def binary_list_to_binary_string(list_of_binary_values):
    return (''.join(list_of_binary_values))

## converts a 8-bit binary array directly to integer value
def binary_list_to_int(list_of_binary_values):
    return int(''.join(list_of_binary_values), 2)

## converts a 8-bit binary string directly to integer value
def binary_string_to_int(binary_string):
    return int((binary_string),2)


