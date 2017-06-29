class RangeExample:

	def find_range(x, y):
		for i in range(x, y):
			print(i)

	find_range(1, 5)

	def find_range_stepwise(x, y, z):
		for i in range(x, y, z):
			print(i)

	find_range_stepwise(0, 100, 4)


