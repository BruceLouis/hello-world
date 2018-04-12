sum = 0
l = []
x = 0

while x < 1000:
	l.append(x)
	x += 1

for num in l:
	if num % 3 == 0 or num % 5 == 0:
		print num
		sum += num

print sum