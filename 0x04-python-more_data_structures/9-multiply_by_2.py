#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for new in new_dict.keys():
        new_dict[new] = new_dict * 2
        return new_dict
