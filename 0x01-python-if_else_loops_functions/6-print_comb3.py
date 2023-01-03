#!/usr/bin/python3
for i in range(0, 10):
    for x in range(1, 10):
        if ((x == i) or (x < i)):
            continue
        elif ((i == 8) and (x == 9)):
            print("89")
        else:
            print("{}{}, ".format(i, x), end="")
