colors = [0, 85, 170, 255]
palette_name = "Blue-Orange"
comment = "Made by Connor Irwin"

file = open(palette_name + ".gpl", "a")

file.write("GIMP Palette\n")
file.write("Name: " + palette_name + "\n")
file.write("# " + comment + "\n")

i = 0
flip = True
string_to_write = ""

for red in colors:
	rs = ""
	for s1 in range (3 - len(str(red))):
		rs += " "

	for green in colors:
		gs = ""
		for s2 in range (4 - len(str(green))):
			gs += " "

		for blue in colors:
			bs = ""
			for s3 in range (4 - len(str(blue))):
				bs += " "

			color_name = "#"
			if len(str(hex(red))) == 3:
				color_name += "0" + str(hex(red))[2]
			else:
				color_name += str(hex(red))[2:4]
			if len(str(hex(green))) == 3:
				color_name += "0" + str(hex(green))[2]
			else:
				color_name += str(hex(green))[2:4]
			if len(str(hex(blue))) == 3:
				color_name += "0" + str(hex(blue))[2]
			else:
				color_name += str(hex(blue))[2:4]

			if flip:
				string_to_write = "\n" + rs + str(red) + gs + str(green) + bs + str(blue) + "  " + color_name + string_to_write
			else:
				string_to_write += rs + str(red) + gs + str(green) + bs + str(blue) + "  " + color_name + "\n"

			i += 1

			if i % len(colors) == 0:
				file.write(string_to_write)
				string_to_write = "\n"
				flip = not flip

file.close()