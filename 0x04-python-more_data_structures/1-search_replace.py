#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list2 = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list2.append(replace)
        else:
            my_list2.append(my_list[i])
    return (my_list2)
