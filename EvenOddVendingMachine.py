class EvenOddVendingMachine(int):


	def vending(x):
		if x % 2 == 0:
			print('Number is even')
		else:
			print('Number is odd')

	def find_range_stepwise(x, y, z):
		for i in range(x, y, z):
			print(i)

	if __name__ == '__main__':
		x = input('Enter a number: ')
		vending(int(x))
		find_range_stepwise(int(x), int(9), int(2))
