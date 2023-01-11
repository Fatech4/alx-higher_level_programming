#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    if my_list is not None:
        for i in range(len(my_list)):
            if my_list[i] is search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
    return new_list
