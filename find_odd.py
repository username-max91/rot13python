#Given an array of integers (seq), function finds the one that appears an odd number of times

def find_it(seq):
    result = []
    for i in seq:
        result.append(seq.count(i))
    for x in result:
        if x % 2 > 0:
            return seq[result.index(x)]