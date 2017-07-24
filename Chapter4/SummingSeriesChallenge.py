from sympy import Symbol, summation, pprint

x = Symbol('x')
n = Symbol('n')


def get_series(n_terms):
	sum = summation(x**n/n, (n, 1, n_terms))
	pprint(sum)
	return sum


def substitute_x(sum):
	sub = float(input('X value to substitute?: '))
	s = sum.subs({x: sub})
	pprint(s)



if __name__ == '__main__':
	n_terms = int(input('Enter number of terms: '))
	sum = get_series(n_terms)
	substitute_x(sum)


