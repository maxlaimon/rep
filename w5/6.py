class Animal():
	__name = "-"
	__age = "-"

	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def get_name(self):
		return self.__name

	def get_age(self):
		return self.__age

	def get_info(self):
		return "Nothing interesting here"


class Zebra(Animal):

	def __init__(self, name, age, height):
		super().__init__(name, age)
		self.__height = height

	def get_height(self):
		return self.__height

	def get_info(self):
		return "Name: {}, Age: {}, height: {}".format(self.get_name(), self.get_age(), self.get_height())


class Dolphin(Animal):

	def __init__(self, name, age, length):
		super().__init__(name, age)
		self.__length = length

	def get_length(self):
		return self.__length

	def get_info(self):
		return "Name: {}, Age: {}, length: {}".format(self.get_name(), self.get_age(), self.get_length())


zebra = Zebra("Spotty", 5, 2)
dolphin = Dolphin("Floppy", 3, 1)


print(zebra.get_info())
print(dolphin.get_info())
