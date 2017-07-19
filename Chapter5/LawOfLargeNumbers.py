import random

def roll(num_trials):
	rolls = []
	for i in range(num_trials):
		rolls.append(random.randint(1, 6))
	return rolls

def calculate_mean(numbers):
	s = sum(numbers)
	N = len(numbers)
	mean = s/N

	return mean

if __name__ == '__main__':
	for trial in [100, 1000, 10000, 100000, 1000000]:
		score = calculate_mean(roll(trial))
		print('Trials: {0} Average: {1}'.format(trial, score))

