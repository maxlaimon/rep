def a():
	print("func a")
	b()
def b():
	print("func b")
	c()
def c():
	raise ValueError('my exception')
	print("func c")
a()
