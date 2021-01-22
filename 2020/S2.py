import sys

row = int(input())
col = int(input())

graph = []
temp = []

for y in range (col - 1):
	a = input()
	temp.append(a)
graph.append(temp)

for x in range (row - 1):
	print(graph[x])
