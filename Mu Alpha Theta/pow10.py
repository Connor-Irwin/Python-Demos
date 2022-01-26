segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 8, 4, 7] # The number 0 is made up of six segments, 5 has five, 12 has seven.
twenties = 0 # Number of times that add up to twenty segments
output = ""
delimiter = "              "

# The PM times
for hour in range(10, 13):
	for minute_tens in range(0, 6):
		for minute_ones in range(0, 10):
			if segments[hour] + segments[minute_tens] + segments[minute_ones] == 20:
				output += str(hour) + ":" + str(minute_tens) + str(minute_ones) + " PM" + delimiter
				twenties += 1


# The AM times
for hour in range(1, 13):
	for minute_tens in range(0, 6):
		for minute_ones in range(0, 10):
			if segments[hour] + segments[minute_tens] + segments[minute_ones] == 20:
				output += str(hour) + ":" + str(minute_tens) + str(minute_ones) + " AM" + delimiter
				twenties += 1

print("These " + str(twenties) + " times have twenty segments:\n\n" + output)