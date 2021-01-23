import sys

row = int(input())
col = int(input())

graph = []
temp = []

size = row * col

for y in range (row):
	k = input().split()
	temp = []
  #print(y)
	for x in k:
		temp.append(x)
	graph.append(temp)

#visited = [False] * 10000001
visited = []
path = []
current_pos = 0
current_path_pos = 0
temp = 0

for x in range (size):
	path.append(-1)

path[current_path_pos] = int(graph[0][0])
print(path[current_path_pos])

if (path[current_path_pos] == graph[row-1][col-1]):
	print("yes")
	sys.exit()
while (path[current_path_pos] != -1):
	#print("here")
	for x in range (1, row + 1):
		print(x, " ", y, " ", size);

		if (path[current_path_pos] % x == 0):
			for y in range (1, col + 1):

				print(x, " ", y, " ", size, " ", path[current_path_pos]);

				if (x * y == path[current_path_pos]):

					temp = int(graph[x-1][y-1])

					#print(x, " ", y, " ", size);
					#print(graph[x-1][y-1], " ", path[current_path_pos], " ", current_path_pos);

					if (x * y == size):
						print("yes")
						sys.exit(0);
					
					if (temp not in visited):
						visited.append(temp)
						path[current_path_pos] = temp

					if ((y+1) > path[current_path_pos] / x):
						break
	current_path_pos += 1
print ("no")
sys.exit(0);
