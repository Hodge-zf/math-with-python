from sympy.plotting import plot
from sympy import Symbol, sympify, solve

def solve_equations(eq1, eq2, x, y):
	solution = solve((eq1, eq2), dict=True)
	if solution:
		print('x: {0} y: {1}'.format(solution[0][x]. solution[1][y]))
	else:
		print('No solution found')
	eq1_y = solve(eq1, 'y')[0]
	eq2_y = solve(eq2, 'y')[0]
	plot(eq1_y, eq2_y, legend=True)

def ask_for_expressions():
	expr1 = input('Enter your first expression in terms of x and y: ')
	expr2 = input('Enter your second expression in terms of x and y: ')
	return expr1, expr2

if __name__ == '__main__':
	expr1, expr2 = ask_for_expressions()
	try:
		expr1 = sympify(expr1)
		expr2 = sympify(expr2)
	except ValueError:
		print('Invalid input')
	else:
		x = Symbol('x')
		y = Symbol('y')
		expr1_symbols = expr1.atoms(Symbol)
		expr2_symbols = expr2.atoms(Symbol)

		if len(expr1_symbols)> 2 or len(expr2_symbols)> 2:
			print('The equations must only have two variables - x and y')
		elif x not in expr1_symbols or y not in expr1_symbols:
			print('First equation must have only x and y variables')
		elif y not in expr2_symbols or y not in expr2_symbols:
			print('Second equation must have only x and y variables')
		else:
			solve_equations(expr1, expr2, x, y)


