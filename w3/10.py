class MyError(Exception):
	def __init__(self, text):
		self.txt = text

a = input("type a positive integer: ")

try:
	a = int(a)
	if a <= 0:
		raise MyError("it's not positive")
except ValueError:
	print("incorrect type of value")
except MyError as m:
	print(m)
else:
	print(a)
