from math import log, cos, sin, pi, floor, ceil
from PIL import Image

class Ellipses:
	# Default values
	def __init__(self):
		self.x_offset = 0
		self.y_offset = 0

		self.x_scale = 1
		self.y_scale = 1

		self.image_width = 100
		self.image_height = self.image_width

		self.size = self.image_width / 2

		self.make_image()

	# Make a blank image or clear the existing one
	def make_image(self):
		self.img = Image.new(mode="L", size=(self.image_width, self.image_height))
		self.pixels = self.img.load()

	# Draw an ellipsis on the blank image
	def draw(self, line_color=255, fill_color=-1):
		x = 0
		while x <= pi / 2:
			x1 = self.size * self.x_scale * sin(x) + self.x_offset + self.image_width / 2
			y1 = self.size * self.y_scale * cos(x) + self.y_offset + self.image_height / 2

			x2 = -x1 + self.image_width - 1
			y2 = -y1 + self.image_height - 1

			x1 = floor(x1)
			y1 = floor(y1)
			x2 = ceil(x2)
			y2 = ceil(y2)

			# *y1* goes out of bounds by 1, one time (*y2* is based on *y1*, so it does as well).
			if 0 <= y1 <= self.image_height - 1:
				if fill_color > -1 and -x1 <= x <= x1:
					for y in range(y2, y1):
						self.pixels[x1, y] = fill_color
						self.pixels[-x1, y] = fill_color

				else:
					self.pixels[x1, y1] = line_color
					self.pixels[x1, y2] = line_color
					self.pixels[x2, y1] = line_color
					self.pixels[x2, y2] = line_color

			x += self.size ** -1

	def show(self):
		self.img.show()

	def save(self, path="image.png"):
		self.img.save(path)

########################################
#           make an ellipsis           #
########################################

ellipsis = Ellipses()
ellipsis.image_width = 20000
ellipsis.image_height = ellipsis.image_width
ellipsis.size = ellipsis.image_width // 2
ellipsis.make_image()
ellipsis.draw(fill_color=255)
ellipsis.show()
# The above setup took 51 seconds to complete # use "try" and "catch" instead of "if" to make it equal between the two
#ellipsis.save(r"C:\Users\conno\Documents\Python\Ellipses drawer\ellipses_drawer_sin.png")