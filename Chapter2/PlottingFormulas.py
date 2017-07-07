import matplotlib.pyplot as plt

def draw_graph(x, y):
	plt.plot(x, y, marker='o')
	plt.xlabel('Distance in meters')
	plt.ylabel('Gravitational force in Newtons')
	plt.title('Gravitational force and distance')
	plt.show()

def generate_F_r():
	r = range(100, 1001, 50)
	F = []
	G = 6.674*(10**-11)
	mass1 = 0.5
	mass2 = 1.5

	for dist in r:
		force = G*(mass1*mass2)/(dist**2)
		F.append(force)

	draw_graph(r, F)

if __name__ == '__main__':
	generate_F_r()