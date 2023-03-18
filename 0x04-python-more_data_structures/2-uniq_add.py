#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_set = set(my_list)
    """ converting the list set to a list."""

    unique_list = list(list_set)

    for num in unique_list:
        print(num)

    result = uniq_add(my_list)
    print("Result: {:d}".format(result))


