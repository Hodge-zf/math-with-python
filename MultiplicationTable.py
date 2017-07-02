class MultiplicationTable:


	def multiplication_table(a):

		for i in range(1, 11):
			print('{0} x {1} = {2}'.format(a, i, a*i))

	if __name__== '__main__':
		a = input('Enter a number: ')
		multiplication_table(float(a))