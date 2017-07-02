class QuadraticRoots:

	def find_roots(a, b, c):

		discriminant = (b*b - 4*a*c)**0.5
		root_1 = (-b + discriminant)/(2*a)
		root_2 = (-b - discriminant) / (2 * a)

		print('Root 1: {0}'.format(root_1))
		print('Root 2: {0}'.format(root_2))

	if __name__ == '__main__':
		a = input('Enter a: ')
		b = input('Enter b: ')
		c = input('Enter c: ')
		find_roots(float(a), float(b), float(c))