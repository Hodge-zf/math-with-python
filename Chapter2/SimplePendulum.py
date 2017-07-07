import matplotlib.pyplot as plt
import math

def draw_graph(x, y):
	plt.plot(x, y, marker='o')
	plt.xlabel('Period in seconds')
	plt.ylabel('Length in meters')
	plt.title('Period of a simple pendulum')
	plt.show()

def generate_T_l():
	l = range(1, 1000, 20)
	T = []
	g = 9.81
	for length in l:
		period = (2*math.pi)*((length/g)**0.5)
		T.append(period)
	draw_graph(T, l)

if __name__ == '__main__':
	generate_T_l()
