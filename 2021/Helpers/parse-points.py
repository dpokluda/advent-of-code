# parse points
lines = [x.strip() for x in open('points.txt', 'r').readlines()]
points = [list(map(int, line.split(','))) for line in lines]

# calculate max (x) and (y) coordinates
max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)
print(max_x, max_y)
# ... or on one line
max_x, max_y = max(p[0] for p in points), max(p[1] for p in points)
print(max_x, max_y)

# create empty board
board = [[0 for x in range(0, max_x)] for y in range(0, max_y)]
print(board)
# ... or using numpy (import numpy as np)
# board = np.zeros((max_y + 1, max_x + 1), dtype=int)

# create special board with increasing numbers
board = [[y*10 + x for x in range(1, 6)] for y in range(1, 6)]
print(board)



