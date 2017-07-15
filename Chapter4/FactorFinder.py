from sympy import factor, pprint, init_printing

init_printing(order='rev-lex')

def factor_eq(expr):

	pprint(factor(expr))

if __name__ == '__main__':
	expr = input('Expression to be factored: ')
	try:
		factor_eq(expr)
	except:
		print('Invalid input')