# 16 - 0 - 10 - 4 - 15
# 0 - 4 - 10 - 15 - 16
# 0 - 4 - 10 = 5
# 4 - 10 - 15 = 5.5
# 10 - 15 - 16 = 3

cities = int(input())

l = []
z = []

current_pos = 0

for x in range (cities):
	l.append(int(input()))

l.sort()

while (current_pos != len(l) - 2):
	current_pos += 1
	h = l[current_pos + 1] - l[current_pos - 1]
	z.append(h / 2)
	#print(z)

z.sort()
print(z[0])

