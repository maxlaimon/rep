def swap(func):
	def wrapper(*args, **kwargs):
		args = reversed(args)
		func(*args, **kwargs)
	return wrapper


@swap
def subtract(a, b, show = False):
	s = a - b
	if show:
		print(s)
	return s


subtract(3, 1, show = True)
