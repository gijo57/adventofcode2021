import numpy as np

with open('input.txt', 'r') as f:
    heights = np.array([list(x) for x in f.read().split('\n')])
    rows = len(heights)
    cols = len(heights[0])


def get_risk_level(low_points):
    return sum(list([int(x)+1 for x in low_points]))


def find_low_points():
    low_points = []
    for i, row in enumerate(heights):
        for j, col in enumerate(row):
            neighbors = []
            if (i == 0):
                if (j == 0):
                    neighbors.extend([heights[i+1, j], heights[i, j+1]])
                elif (j == cols - 1):
                    neighbors.extend([heights[i, j-1], heights[i+1, j]])
                elif (j > 0 and j < cols - 1):
                    neighbors.extend([heights[i, j+1], heights[i, j-1], heights[i+1, j]])
            elif (i == rows - 1):
                if (j == 0):
                    neighbors.extend([heights[i-1, j], heights[i, j+1]])
                elif (j == cols - 1):
                    neighbors.extend([heights[i, j-1], heights[i-1, j]])
                elif (j > 0 and j < cols - 1):
                    neighbors.extend([heights[i, j+1], heights[i, j-1], heights[i-1, j]])
            elif (i > 0 and i < rows - 1):
                if (j == 0):
                    neighbors.extend([heights[i-1, j], heights[i+1, j], heights[i, j+1]])
                elif (j == cols - 1):
                    neighbors.extend([heights[i-1, j], heights[i+1, j], heights[i, j-1]])
                elif (j > 0 and j < cols - 1):
                    neighbors.extend([heights[i-1, j], heights[i+1, j], heights[i, j-1], heights[i, j+1]])
            if (col < min(neighbors)):
                low_points.append(col)
    return low_points


answer1 = get_risk_level(find_low_points())
print(answer1)