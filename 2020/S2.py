from sys import stdin, stdout
from sympy import factorint, primefactors
from itertools import permutations
import numpy as np

rows = int(stdin.readline())
cols = int(stdin.readline())

k = []

for y in range(rows):
  k.append(stdin.readline().split())

startx, starty = 0, 0
endx, endy = cols - 1, rows - 1
currentx, currenty = endx, endy

while (currentx != 0 and currenty != 0):
  currentsquare = int(k[currenty][currentx])
  goto = (currentx + 1) * (currenty + 1)

  array = np.array(k)

  locations = np.argwhere(array == str(goto))

  print(locations)
