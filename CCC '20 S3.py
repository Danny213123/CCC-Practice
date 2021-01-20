p = {}
c = []
d = []

k = input()
b = input()

previous = ""

for x in range (len(k)):
	if (k[x:x+1] != previous):
		c.append(k[x:x+1])
		p[k[x:x+1]] = k.count(k[x:x+1])
		previous = k[x:x+1]
correct = 0

#print(p)
#print(c)

if (len(b) < len(k)):
	print(correct)
else:
	for x in range (len(b) - len(k) + 1):
		word2 = b[x:x+len(k)]
		word = set(word2)
		true = 0
		if (len(word) == len(p)):
			for y in word:
				if (y in c):
					if (word2.count(y) == p[y]):
						true += 1
			if (true == len(word) and word2 not in d):
				correct += 1
				d.append(word2)
	#print(d)
	print(correct)
