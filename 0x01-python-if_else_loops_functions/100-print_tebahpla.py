#!/usr/bin/python3
f = 0
for i in range(122, 98, -1):
    print("{}".format(chr(i - f)), end="")
    if f == 0:
        f = 32
    else:
        f = 0
