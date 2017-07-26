from matplotlib import pyplot as plt


def draw_square():
	ax = plt.axes(xlim = (0, 6), ylim = (0, 6))
	square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed = True)
	ax.add_patch(square)



def create_circle(x, y):
	circle = plt.Circle((x, y), radius = 0.5, color = 'white')
	return circle

def draw_circle(circle):
	ax = plt.gca()
	ax.add_patch(circle)
	plt.axis('scaled')

if __name__ == '__main__':
	draw_square()
	y = 1.5
	while y < 5:
		x = 1.5
		while x < 5:
			c = draw_circle(create_circle(x, y))
			x += 1.0
		y+= 1.0
	plt.show()
