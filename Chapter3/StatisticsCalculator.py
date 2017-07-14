from collections import Counter

def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N

	return mean

def calculate_median(numbers):
	N = len(numbers)
	numbers.sort()

	if N % 2 == 0:
		m1 = N/2
		m2 = (N/2) + 1

		m1 = int(m1) - 1
		m2 = int(m2) - 1
		median = (numbers[m1] + numbers[m2])/2
	else:
		m = (N+1)/2
		m = int(m) - 1
		median = numbers[m]

	return median

def calculate_mode(numbers):
	c = Counter(numbers)
	numbers_freq = c.most_common()
	max_count = numbers_freq[0][1]

	modes = []
	for num in numbers_freq:
		if num[1] == max_count:
			modes.append(num[0])
	return modes

def find_differences(numbers):
	mean = calculate_mean(numbers)
	diff = []
	for num in numbers:
		diff.append(num-mean)

	return diff

def calculate_variance(numbers):

	diff = find_differences(numbers)
	squared_diff = []
	for d in diff:
		squared_diff.append(d**2)
	sum_squared_diff = sum(squared_diff)
	variance = sum_squared_diff/len(numbers)
	return variance

if __name__ == '__main__':

	x = (input('Filename: '))
	numbers = []
	with open(x) as i:
		for line in i:
			numbers.append(int(line))
	N = len(numbers)
	mean = calculate_mean(numbers)
	median = calculate_median(numbers)
	modes = calculate_mode(numbers)
	variance = calculate_variance(numbers)
	std = variance ** 0.5
	print('The mean of the set of {0} numbers is {1}'.format(N, mean))
	print('The median of the set of {0} numbers is {1}'.format(N, median))
	print('The mode(s) of the set of numbers are: ')
	for mode in modes:
		print(mode)
	print('The variance of the list of numbers is {0}'.format(variance))
	print('The standard deviation of the list of numbers is {0}'.format(std))