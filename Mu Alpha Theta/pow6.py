combinations = [] # (r, g, b)
max_r = 0
max_g = 0
max_b = 0

for g in range(1, 21):
	for r in range(1, 13):
		for b in range(1, 9):
			if (r + g + b) % 13 == 0:
				combinations.append((r, g, b))

				if max_r < r:
					max_r = r

				if max_g < g:
					max_g = g

				if max_b < b:
					max_b = b

print("Max r: " + str(max_r))
print("Max g: " + str(max_g))
print("Max b: " + str(max_b))

print(str(len(combinations)), "combinations are divisible by 13")
print(str(len(combinations) / 1920 * 100) + "%")
