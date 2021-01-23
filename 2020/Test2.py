import sys

row = int(input())
col = int(input())

graph = []
temp = []

size = row * col

graph.append("")
for y in range (1, row + 1):
	k = input().split()
	temp = []
  #print(y)
	temp.append(" ")
	for x in k:
		temp.append(x)
	graph.append(temp)

visited = []
path = []
current_pos = 0
current_path_pos = 0
target = row * col
temp = 0

for x in range (size):
	path.append(-1)

path[current_path_pos] = graph[1][1]
