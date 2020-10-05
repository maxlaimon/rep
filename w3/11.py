def a():
	print("func a")
def b():
	print("func b")
def c():
	raise ValueError('my exception')
	print("func c")
a()
b()
c()
