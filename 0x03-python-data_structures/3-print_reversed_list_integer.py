#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ if statement checks if the list of intergers is empty."""
    if not my_list:
        pass 

    else:
        for nums in my_list:
            nums.reverse()
            print("{:d}".format(nums))
