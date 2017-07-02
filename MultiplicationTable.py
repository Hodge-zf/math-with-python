class MultiplicationTable:


	def multiplication_table(a, b):

		for i in range(1, b):
			print('{0} x {1} = {2}'.format(a, i, a*i))

	if __name__== '__main__':
		a = input('Enter a number: ')
		b = input('Enter value for range: ')
		multiplication_table(float(a), int(b))