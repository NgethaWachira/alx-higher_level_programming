#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    result = 1

    for x in new_dict:
        result = result * new_dict[x]
        return result
