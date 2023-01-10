#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        tuple_fcl = (0, None)
    else:
        tuple_fcl = (len(sentence), sentence[0])
    return (tuple_fcl)


