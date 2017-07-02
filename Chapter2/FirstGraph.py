from pylab import plot, show

class FirstGraph:

	def graphCoords(x_coords, y_coords):
		plot(x_coords, y_coords)
		show()

	if __name__ == '__main__':
		x = [int(a) for a in input('x coordinates: ').split()]
		y = [int(a) for a in input('y coordinates: ').split()]
		graphCoords(x, y)

