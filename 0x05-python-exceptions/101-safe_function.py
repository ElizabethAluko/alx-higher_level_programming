#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        fun = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return (None)
    else:
        return (fun)
