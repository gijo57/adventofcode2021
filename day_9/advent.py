import numpy as np
from functools import reduce

with open('input.txt', 'r') as f:
    heights = np.array([list(x) for x in f.read().split('\n')])
    rows = len(heights)
    cols = len(heights[0])


def get_neighbors(i, j):
    neighbors = []
    if (i == 0):
        if (j == 0):
            neighbors.extend([(heights[i+1, j],[i+1, j]), (heights[i, j+1],[i, j+1])])
        elif (j == cols - 1):
            neighbors.extend([(heights[i, j-1],[i, j-1]), (heights[i+1, j],[i+1, j])])
        elif (j > 0 and j < cols - 1):
            neighbors.extend([(heights[i, j+1],[i, j+1]), (heights[i, j-1],[i, j-1]), (heights[i+1, j],[i+1, j])])
    elif (i == rows - 1):
        if (j == 0):
            neighbors.extend([(heights[i-1, j],[i-1, j]), (heights[i, j+1],[i, j+1])])
        elif (j == cols - 1):
            neighbors.extend([(heights[i, j-1],[i, j-1]), (heights[i-1, j],[i-1, j])])
        elif (j > 0 and j < cols - 1):
            neighbors.extend([(heights[i, j+1],[i, j+1]), (heights[i, j-1],[i, j-1]), (heights[i-1, j],[i-1, j])])
    elif (i > 0 and i < rows - 1):
        if (j == 0):
            neighbors.extend([(heights[i-1, j],[i-1, j]), (heights[i+1, j],[i+1, j]), (heights[i, j+1],[i, j+1])])
        elif (j == cols - 1):
            neighbors.extend([(heights[i-1, j],[i-1, j]), (heights[i+1, j],[i+1, j]), (heights[i, j-1],[i, j-1])])
        elif (j > 0 and j < cols - 1):
            neighbors.extend([(heights[i-1, j],[i-1, j]), (heights[i+1, j],[i+1, j]), (heights[i, j-1],[i, j-1]), (heights[i, j+1],[i, j+1])])
    return neighbors


def find_low_points():
    low_points = []
    for i, row in enumerate(heights):
        for j, col in enumerate(row):
            neighbors = [x[0] for x in get_neighbors(i, j)]
            if (col < min(neighbors)):
                low_points.append((col, [i, j]))
    return low_points


def get_risk_level(low_points):
    return sum(list([int(x)+1 for x in low_points]))


def find_basin(x, y, input):
    basin = []
    visited = []
    queue = [[x, y]]

    while queue:
        current = queue.pop()
        if current in visited:
            continue
        else:
            visited.append(current)
            if input[current[0]][current[1]] != '9':
                basin.append(current)
                queue.extend([list(a)[1] for a in get_neighbors(current[0], current[1]) if a[1] not in visited])
    return len(basin)


low_points = [x[1] for x in find_low_points()]
basins = [find_basin(x, y, heights) for [x, y] in low_points]
answer1 = get_risk_level([x[0] for x in low_points])
answer2 = reduce(lambda x, y: x * y, sorted(basins)[-3:])

print(answer1, answer2)
