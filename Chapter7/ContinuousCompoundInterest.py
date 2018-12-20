from sympy import Limit, Symbol, S

n = Symbol('n')
print(Limit((1+1/n)**n, n, S.Infinity).doit())

