NumberGrid = [1, 2],[3, 4]

Sequence = input()

for x in range (len(Sequence)):
    if (Sequence[x] == "V"):
        NumberGrid[0][0], NumberGrid[0][1] = NumberGrid[0][1], NumberGrid[0][0] 
        NumberGrid[1][0], NumberGrid[1][1] = NumberGrid[1][1], NumberGrid[1][0] 
    else:
        NumberGrid[0][0], NumberGrid[1][0] = NumberGrid[1][0], NumberGrid[0][0] 
        NumberGrid[1][1], NumberGrid[0][1] = NumberGrid[0][1], NumberGrid[1][1] 

print (NumberGrid[0][0], NumberGrid[0][1])
print (NumberGrid[1][0], NumberGrid[1][1])
