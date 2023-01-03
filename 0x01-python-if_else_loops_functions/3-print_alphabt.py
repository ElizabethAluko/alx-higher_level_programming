#!/usr/bin/python3
for n in range(97, 123):
    if ((n == 113) or (n == 101)):
        continue
    else:
        print("{}".format(chr(n)), end="")
