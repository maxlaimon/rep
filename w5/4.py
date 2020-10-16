class Shape():

	def __init__(self, height, width):
		self.height = height
		self.width = width

	def get_area(self):
		raise NotImplementedError()


class Triangle(Shape):

	def get_area(self):
		area = (self.height * self.width) / 2
		return area


class Rectangle(Shape):

	def get_area(self):
		area = self.height * self.width
		return area


t = Triangle(3, 4)
r = Rectangle(3, 4)

print(t.get_area())
print(r.get_area())
