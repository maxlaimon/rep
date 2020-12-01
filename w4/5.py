def dec(func):
	def wrapper(*args, **kwargs):
		num = func(*args, **kwargs)
		if not num:
			return('Нет(')
		elif num > 10:
			return('Очень много')
		else:
			return num
	return wrapper


@dec
def f(in_list):
	i = 0
	for n in in_list:
		if n % 2 == 0:
			i += 1
	return i


print(f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f([2, 4, 8, 10, 12, 16, 24, 26, 28, 30, 32, 34, 36]))
print(f([1, 3, 5]))
