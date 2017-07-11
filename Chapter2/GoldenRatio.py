import matplotlib.pyplot as plt

def fibo(n):
	if n == 1:
		return [1]
	if n == 2:
		return [1, 1]
	a = 1
	b = 1
	series = [a, b]
	for i in range(n):
		c = a + b
		series.append(c)
		a = b
		b = c

	return series

if __name__ == '__main__':
	plt.plot(fibo(int(input('Range: '))), marker = '+')
	plt.xlabel('Entry')
	plt.ylabel('Value')
	plt.title('Fibonacci numbers')
	plt.show()