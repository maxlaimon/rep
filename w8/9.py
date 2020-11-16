from itertools import starmap, product

def quad_sum(*args):
    qsum = [i*i for i in args]
    return(sum(qsum))

def maximize(lists, m):
    max = 0
    for i in starmap(quad_sum, list(product(*lists))):
        if i % m > max:
            max = i % m
    return max
