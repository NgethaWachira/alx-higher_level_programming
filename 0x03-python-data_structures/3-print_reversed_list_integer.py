#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for nums in my_list:
        nums.reverse()
        print("{:d}".format(nums))
