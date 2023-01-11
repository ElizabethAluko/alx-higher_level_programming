#!/usr/bin/python3

def best_score(a_dictionary):
    initK = list(a_dictionary.keys())[0]
    maxV = a_dictionary[initK]
    for k, v in a_dictionary.items():
        if v > maxV:
            maxV = v
            initK = k
    return (initK)
