class ComplexNumbers:

	#python supports complex numbers, but uses the letter j instead of i
	#both the real and imaginary parts are floating point by default

	x = 2 + 3j
	y = 3 + 3j

	print(x)
	print(x+y)
	print(y-x)
	print(x*y)
	print(x/y)

	#the real and imaginary parts can be returned by calling .real and .imag
	print(x.real)
	print(y.imag)

	#complex conjugation can be performed by the conjugate() method
	print(x.conjugate())

	#to find a complex number's magnitude, we can utilize the abs() method
	print(abs(x))