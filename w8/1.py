import math
import numpy as np

arr = [np.pi, 0, 1]

def print_map(function, iterable):
    for i in iterable:
        print(function(i))

def print_map_new(function, iterable):
	print(*(map(function, iterable)), sep = '\n')

print_map(math.sin, arr)
print_map_new(math.sin, arr)
