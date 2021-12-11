import numpy as np

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


def find_basins(low_points):
    basins = []
    for point in low_points:
        basins.append(get_basin(point))
    return basins

def get_basin(point):
    basin_size = 1
    neighbors = get_neighbors(point[0], point[1])
    print(neighbors)
    for n in neighbors:
        value = int(n[0])
        coords = n[1]
        if (value != 9):
            basin_size += 1
    return basin_size


answer1 = get_risk_level([x[0] for x in find_low_points()])
print(find_basins([x[1] for x in find_low_points()]))
print(answer1)
