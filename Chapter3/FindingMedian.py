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

if __name__ == '__main__':
	grades = [97, 85, 91, 93, 72, 90, 54, 87]
	median = calculate_median(grades)
	N = len(grades)
	print('Median grade for {0} assignments is is {1}'.format(N, median))
