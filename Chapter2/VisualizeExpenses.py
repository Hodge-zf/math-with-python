import matplotlib.pyplot as plt

def create_bar_chart(data, labels):
	num_bars = len(data)
	positions =  range(1, num_bars+1)
	plt.barh(positions, data, align='center')
	plt.yticks(positions, labels)
	plt.xlabel('Dollars')
	plt.ylabel('Expense')
	plt.title('Monthly expenses')
	plt.grid()
	plt.show()

if __name__ == '__main__':
	try:
		labels = [i for i in input('Expense names: ').split()]
		data = [i for i in input('Dollar amounts: ').split()]
	except ValueError:
		print('Invalid input')
	else:
		create_bar_chart(data, labels)
		