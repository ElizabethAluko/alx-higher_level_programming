#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            if i.isdigit() and count < x:
                print("{:d}".fomart(i), end="")
                count += 1
            else:
                continue
        print ()
        return (count)
    except Indexerror:
