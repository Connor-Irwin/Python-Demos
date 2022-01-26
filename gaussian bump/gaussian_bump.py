from math import exp, sqrt
from PIL import Image

def bump(x, y, x0=0, y0=0, sX=1, sY=1): # A ℯ^(-((x - x_{0})² / (2σ_{X}²) + (y - y_{0})² / (2σ_{y}²)))
	return exp(-(((x - x0)**2)/(2 * sX**2) + ((y - y0)**2)/(2 * sY**2)))

def colorize(num):
	color = [0, 0, 0]
	for i in range(3):
			color[i] = round(num % 256)
			num //= 256
	return((color[0], color[1], color[2]))

n = 5																			# This sets *image_width* to the
image_width = int((((1 + sqrt(5)) / 2)**n - ((1 - sqrt(5)) / 2)**n) / sqrt(5))	# nth term of the fibonacci sequence (1597 is the 17th)
image_height = image_width

scale = .0849321801 * image_width + 0.00000054293 # This finds the best scale for a given diameter (found with stat calc)

img = Image.new(mode="RGB", size=(image_width, image_height))
pixels = img.load()

x = 0

while x < image_width:
	y = 0

	while y < image_height:
		color = bump(x, y, (image_width - 1) / 2, (image_height - 1) / 2, scale, scale)

		pixels[x, y] = colorize((1 - color) * (255 + 255*256 + 255*256**2))

		y += 1
	x += 1

# True if the pixel right outside of the image is full white
print(colorize((1 - bump(image_width, 0, (image_width - 1) / 2, (image_height - 1) / 2, scale, scale)) * (255 + 255*256 + 255*256**2)) == (255, 255, 255))

img.save("gaussian bump/image.png")