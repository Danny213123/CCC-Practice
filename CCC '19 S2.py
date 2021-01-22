inputs = int(input())
l = []

for x in range (inputs):
	l.append(int(input()))

def p(n):
	if (n < 2):
		return False
	else:
		for x in range (2, int(n) - 1):
			if (int(n) % x == 0):
				return False
		return True

for z in range (len(l)):
	y, c = 0, l[z] * 2
	
	for x in range (213213213):
		y += 1
		c -= 1
		#print(p(y), p(c))
		if ((y + c) / 2 == l[z] and p(y) == True and p(c) == True):
			break
		#print(y, c)
	print(y, c)
