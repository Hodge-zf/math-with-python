from sympy import Limit, Symbol, S

x = Symbol('x')

print(Limit(1/x, x, S.Infinity).doit())

