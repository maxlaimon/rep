import math
import cmath

class MyMath:

	pi = 3.14
	_complex = False

	@staticmethod
	def sin(x):
		return math.sin(x)

	@classmethod
	def is_complex(cls):
		return cls._complex

	@classmethod
	def sqrt(cls, x):
		if cls.is_complex():
			complex = cmath.sqrt(x)
			return (complex.real, complex.imag)
		elif x >= 0:
			return math.sqrt(x)
		else:
			raise ValueError("can't extract sqrt from negative number")


class MyComplexMath(MyMath):

	_complex = True
