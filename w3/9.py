try:
	int("a")
except ValueError:
	print("can't be int'ed")
finally:
	print("reached \"finally\"")
