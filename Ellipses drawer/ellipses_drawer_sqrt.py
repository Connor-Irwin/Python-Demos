from math import sqrt, floor, ceil, log, pi
from PIL import Image

class Ellipses:
	def __init__(self):
		self.x_offset = 0
		self.y_offset = 0

		self.x_scale = 1
		self.y_scale = 1

		self.image_width = 100
		self.image_height = 100

		self.size = (self.image_width / 2) ** 2

	def make_image(self):
		self.img = Image.new(mode="L", size=(self.image_width, self.image_height))
		self.pixels = self.img.load()

	def draw(self, fill = -1):
		x = 0
		#for x in range(ceil(self.image_width / 2 + 1)):
		while x <= self.image_width / 2 + 1:
			try:
				y1 = self.y_scale * sqrt(self.size - (self.x_scale ** -1 * x - self.x_offset / self.x_scale) ** 2)

				y2 = round(-y1 + self.y_offset + self.image_height / 2)
				y1 = round(y1 + self.y_offset + self.image_height / 2)
				x1 = round(x + self.image_width / 2)
				x2 = round(-x + self.image_width / 2)

				if fill > -1:
					for y in range(y2, y1):
						self.pixels[x1, y] = fill
						self.pixels[x2, y] = fill

				else:
					self.pixels[x1, y1] = 255
					self.pixels[x1, y2] = 255
					self.pixels[x2, y1] = 255
					self.pixels[x2, y2] = 255

			except:
				pass

			x += 1

	def show(self):
		self.img.show()

########################################
#           make an ellipsis           #
########################################

ellipsis = Ellipses()

ellipsis.image_width = 20000
ellipsis.image_height = ellipsis.image_width
ellipsis.size = (ellipsis.image_width // 2) ** 2
ellipsis.make_image()

'''
ellipsis.size = (ellipsis.image_width / 2) ** 2
#ellipsis.size /= ellipsis.y_scale ** 2
ellipsis.draw(25)

ellipsis.size /= 5
ellipsis.size /= ellipsis.y_scale ** 2
ellipsis.draw(50)

ellipsis.show()
'''
'''
thing = (ellipsis.image_width / 2) ** 2
thing_original = thing
while thing > 0:
	ellipsis.size = thing
	ellipsis.draw()
	#ellipsis.draw(round(255 * log(thing, thing_original)))
	#ellipsis.draw(round(thing_original * thing ** -1))
	thing -= 25
'''
ellipsis.draw(fill=255)
ellipsis.show()
# The above setup took 39 seconds to complete
