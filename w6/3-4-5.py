import math
import cmath


class MyMath:

	pi = 3.14
	_complex = False #инкапсуляция

	@staticmethod
	def sin(x): #наследование(sin не реализован в дочернем классе, но его можно вызвать)
		return math.sin(x)

	@classmethod
	def is_complex(cls):
		return cls._complex

	@classmethod
	def sqrt(cls, x): #наследование(аналогично с sin)
		if cls.is_complex(): #полиморфизм
			complex = cmath.sqrt(x)
			return (complex.real, complex.imag)
		elif x >= 0:
			return math.sqrt(x)
		else:
			raise ValueError("can't extract sqrt from negative number")


class MyComplexMath(MyMath): #наследование

	_complex = True #инкапсуляция


print(MyComplexMath.sqrt(-9))
print(MyMath.sqrt(-9))


#используется классовый метод, т к вывод метода _complex
#зависит от того, в каком классе мы его вызываем
