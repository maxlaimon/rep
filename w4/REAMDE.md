# 1
```python
import sys

print(len(sys.argv) - 1)
print(sys.argv)
```
In: 
```
python3 1.py asdf 1234
```
Out: 
```2
['1.py', 'asdf', '1234']
```
# 2
```python
import sys

print(sys.platform)
print(sys.version)
```
Out:
```
linux
3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0]x
```
# 3
```python
import argparse


def create_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', type = int)

	return parser


def fib(n):
	if n in (1, 2):
		return 1
	else:
		return fib(n - 1) + fib(n - 2)


parser = create_parser()
namespace = parser.parse_args()

print(fib(namespace.n))
```
In:
```
python3 3.py -n 6
```
Out:
```
8
```
# 4
```python
import math
import sys
import argparse


def createParser():
	parser = argparse.ArgumentParser()
	parser.add_argument('N', type = int)
	parser.add_argument('--show-all', '-a', action='store_true', default = False)
	parser.add_argument('--file', '-f', type = argparse.FileType('w'))

	return parser


def eratosthenes(n):
	n = int(1.5 * n * math.log(n))
	sieve = list(range(n + 1))
	sieve[1] = 0
	for i in sieve:
		if i > 1:
			for j in range(i + i, len(sieve), i):
				sieve[j] = 0

	sieve = list(filter(lambda x: x != 0, sieve))

	return sieve


parser = createParser()
namespace = parser.parse_args(sys.argv[1:])
primes = eratosthenes(namespace.N)
print(primes[-1])

if namespace.show_all:
	print(*primes)

	if namespace.file is not None:
		for i in primes:
			namespace.file.write(str(i) + '\n')
else:
	if namespace.file is not None:
		namespace.file.write(str(primes[-1]))
```
In:
```
python3 4.py -a 10
```
Out:
```
31
2 3 5 7 11 13 17 19 23 29 31
```
In:
```
python3 4.py -f 4.txt -a 15
```
Out:
```
59
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59
```
4.txt:
```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
```
# 5
```python
def dec(func):
	def wrapper(in_list):
		num = func(in_list)
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


print(f([1,2,3,4,5,6,7,8,9,10]))
print(f([2,4,8,10,12,16,24,26,28,30,32,34,36]))
print(f([1,3,5]))
```
Out:
```
5
Очень много
Нет(
```
# 6
```python
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
```
Out:
```
-2
```
# 7
```python
import time
from datetime import datetime
from functools import wraps


def logger(file):
	def dec(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			start = time.time()
			f(*args, **kwargs)
			stop = time.time()
			timeinwork = stop - start
			start, stop = datetime.fromtimestamp(start), datetime.fromtimestamp(stop)
			returned = f(*args, **kwargs) if f(*args, **kwargs) is not None else '-'

			with open(file, "w") as log:
				log.write(
				"called at {}\narguments: {}\nreturned: {}\nended at: {}\nexecution time:{}\n".format(start, args, returned, stop, timeinwork))

			return f(*args, **kwargs)
		return wrapper
	return dec


@logger("log.txt")
def func(a, b):
        return a + b

func(2, 3)
```
log.txt:
```
called at 2020-10-11 23:24:18.035919
arguments: (2, 3)
returned: 5
ended at: 2020-10-11 23:24:18.035920
execution time:7.152557373046875e-07
```
