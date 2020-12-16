import sys

input_storage = []
grid = []

# . = clear
# # = blocked
#  make current square #
#   while true:
#   while (grid[currentx + 1][currenty ] != "#""): currentx += 1
#   while (grid[currentx][currenty + 1] != "#"): currenty += 1
#   while (grid[currentx])

def get_grid():
  for x in range (len(grid)):
    print(grid[x])

for x in range (5):
  input_storage.append(int(input()))

currentx, currenty, = input_storage[2], 0

# Initialize grid
for i in range (input_storage[1]):
  temp_grid = ["#"] * (input_storage[0] + 2)
  for j in range (input_storage[0]):
    temp_grid[j] = "."
  grid.append(temp_grid)

# Set up top blocked area
for x in range (1, input_storage[3] + 1):
  for y in range (1, input_storage[2] + 1):
    grid[x][0] = "#"
    grid[x][y] = "#"
    grid[x][len(grid[0]) - y - 1] = "#"

# Set up bottom blocked area
for x in range (len(grid) - input_storage[3], len(grid)):
  for y in range (1, input_storage[2] + 1):
    grid[x][y] = "#"
    grid[x][len(grid[0]) - y - 1] = "#"

total_moved = 0

print(len(grid[0]))
print(len(grid))
print(input_storage[4])

# REMEMBER: it's grid[y][x]

#and currentx < len(grid[0])

while (total_moved != input_storage[4]):
  grid[currenty][currentx] = "M"

  # Move right
  if (currentx != len(grid[0]) - 1):
    print("hi1")
    while (grid[currenty][currentx + 1] != "#"):
      grid[currenty][currentx] = "#"
      currentx += 1
      if (currentx == len(grid[0]) - 1):
        break
      total_moved += 1
      if (total_moved == input_storage[4]):
        grid[currenty][currentx] = "M"
        get_grid()
        print(currenty + 1, currentx + 1)
        sys.exit()
      grid[currenty][currentx] = "M"

  # Go down
  print("hi2")
  while (grid[currenty][currentx + 1] == "#"):
    grid[currenty][currentx] = "#"
    currenty += 1
    total_moved += 1
    if (total_moved == input_storage[4] - 1):
      grid[currenty - 1][currentx] = "M"
      get_grid()
      print(currenty + 1, currentx + 1)
      sys.exit()
    grid[currenty][currentx] = "M"

  # Move right
  if (currentx != len(grid[0]) - 1):
    print("hi3")
    while (grid[currenty][currentx + 1] != "#"):
      grid[currenty][currentx] = "#"
      currentx += 1
      if (currentx == len(grid[0]) - 1):
        break
      total_moved += 1
      if (total_moved == input_storage[4] - 1):
        grid[currenty][currentx] = "M"
        get_grid()
        print(currenty + 1, currentx + 1)
        sys.exit()
      grid[currenty][currentx] = "M"
  
  # Move down
  print("hi4")
  while (grid[currenty + 1][currentx] == "."):
    grid[currenty][currentx] = "#"
    currenty += 1
    total_moved += 1
    if (total_moved == input_storage[4] - 1):
      grid[currenty][currentx] = "M"
      get_grid()
      print(currenty + 1, currentx + 1)
      sys.exit()
    grid[currenty][currentx] = "M"

  # Move left
  if (currenty != 0):
    print("hi5")
    while (grid[currenty + 1][currentx] == "#"):
      grid[currenty][currentx] = "#"
      currentx -= 1
      if (currentx == 0):
        break
      total_moved += 1
      if (total_moved == input_storage[4] - 1):
        grid[currenty][currentx] = "M"
        get_grid()
        print(currenty + 1, currentx + 1)
        sys.exit()
  
  # Move down
  if (currenty == len(grid)):
    while (grid[currenty][currentx + 1] == "#"):
      print("hii")
      grid[currenty][currentx] = "#"
      currenty += 1
      if (currenty == len(grid) - 1):
        break
      total_moved += 1
      if (total_moved == input_storage[4] - 1):
        grid[currenty - 1][currentx] = "M"
        get_grid()
        print(currenty + 1, currentx + 1)
        sys.exit()

  while (grid[currenty][currentx + 1] == "#"):
    grid[currenty][currentx] = "#"
    currenty += 1
    total_moved += 1
    if (total_moved == input_storage[4] - 1):
      grid[currenty - 1][currentx] = "M"
      get_grid()
      print(currenty + 1, currentx + 1)
      sys.exit()
    grid[currenty][currentx] = "M"



get_grid()
