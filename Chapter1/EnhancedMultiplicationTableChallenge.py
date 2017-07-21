def enhanced_mt(a, b):

	for i in range(1, b):
		print('{0} x {1} = {2}'.format(a, i, a*i))

if __name__ == '__main__':

	while True:
		enhanced_mt(float(input('Enter a number: ')), int(input('Enter value for range: ')))

		answer = input('Do you want to exit? (y) for yes: ')
		if answer == 'y':
			break