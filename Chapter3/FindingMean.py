def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N

	return mean

if __name__ == '__main__':

	grades = [97, 85, 91, 93, 72, 90, 54, 87]
	mean = calculate_mean(grades)
	N = len(grades)
	print('Grade average for {0} assignments is is {1}'.format(N, mean))