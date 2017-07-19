from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
import csv


def draw_venn(f, o):
	venn2(subsets=(f, o),set_labels=('Football', 'Others'))
	plt.show()

def read_csv(filename):
	football = []
	others = []
	with open(filename) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			football.append(row[1])
			others.append(row[2])
		return football, others

if __name__ == '__main__':
	football, others = read_csv(input('Filename: '))
	f = FiniteSet(*football)
	o = FiniteSet(*others)
	draw_venn(f, o)