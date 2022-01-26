from math import exp, sqrt
from PIL import Image

def bump(x, y, x0=0, y0=0, sX=1, sY=1):
	return exp(-(((x - x0)**2)/(2 * sX**2) + ((y - y0)**2)/(2 * sY**2)))

def colorize(num):
	color = [0, 0, 0]
	for i in range(3):
			color[i] = round(num % 256)
			num //= 256
	return((color[0], color[1], color[2]))

radius = 1597/2
increment = .000001
scale = 135.6
while True:
	edge = colorize(bump(radius, 0, 0, 0, scale, scale) * (255 + 255*256 + 255*256**2))

	if edge == (0, 0, 0):
		scale += increment

	else:
		print(scale)
		break

print(colorize(bump(radius + 1, 0, 0, 0, scale, scale) * (255 + 255*256 + 255*256**2)))