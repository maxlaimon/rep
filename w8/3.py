def my_map(function, iterable):
	for i in iterable:
		yield function(i)

def my_enumerate(iterable, start = 0):
	for i in iterable:
		yield start, i
		start += 1

def my_zip(*iterables):
	iterlen = list(map(len, iterables))
	minlen = min(iterlen)
	for i in range(minlen):
		yield tuple(j[i] for j in iterables)

a = (1, 2, 3)
b = (4, 5, 6)
z = my_zip(a, b)
print(list(z))
