num = int(input("Enter a number to be converted to base 15: "))

mod = num % 15
output = ""

while num > 0:
	output = str(mod) + " " + output #chr(mod + 65) + output
	num //= 15
	mod = num % 15

print(output)