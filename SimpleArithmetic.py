class SimpleArithmetic:


	def SimpleAdd(x,y):
		return x+y


	def SimpleSubtract(x,y):
		return x-y


	def SimpleMultiply(x,y):
		return x*y


	def SimpleDivide(x,y):
		return x/y


	def FloorDivide(x,y):
		#the double-slash operator performs division and then rounds the result down to the next-lowest integer
		#this provides interesting results when combined with negative products
		return x//y


	def SimpleModulus(x,y):
		return x%y


	def SimplePower(x,y):
		return x**y

	print(SimpleAdd(1,2))
	print(SimpleSubtract(2,1))
	print(SimpleMultiply(1.5,3.5))
	print(SimpleDivide(10,3))
	print(FloorDivide(-3,2))
	print(SimpleModulus(9,2))
	print(SimplePower(8,2))