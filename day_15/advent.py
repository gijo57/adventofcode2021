from collections import defaultdict
from copy import deepcopy
import numpy as np

with open('input.txt', 'r') as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    rows1 = len(lines)
    cols1 = len(lines[0])


def find_neighbors(x, y, rows, cols, lines):
    neighbors = defaultdict()
    x_vals = [-1, 0, +1]
    y_vals = [-1, 0, +1]
    for x2 in x_vals:
        for y2 in y_vals:
            if (y + y2 >= 0 and x + x2 >= 0 and y + y2 < cols and x + x2 < rows):
                if (x, y) != (x + x2, y + y2):
                    if (x2 == 0 or y2 == 0):
                        neighbors[(x + x2, y + y2)] = lines[x + x2][y + y2]
    return neighbors


def define_risks(rows, cols, lines):
    risks = defaultdict()
    for x in range(rows):
        for y in range(cols):
            risks[(x, y)] = find_neighbors(x, y, rows, cols, lines)
    return risks


def create_nodes(rows, cols):
    nodes = []
    for x in range(rows):
        for y in range(cols):
            nodes.append((x, y))
    return nodes


def create_larger_map():
    map = np.array(lines)
    for i in range(4):
        new_part = lines
        for a in range(len(lines)):
            for b in range(len(lines[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=0)
    new_part = deepcopy(map)
    for i in range(4):
        for a in range(len(new_part)):
            for b in range(len(new_part[0])):
                new_part[a][b] += 1
                if (new_part[a][b] > 9):
                    new_part[a][b] = 1
        map = np.concatenate((map, np.array(new_part)), axis=1)
    return map


def dijkstra(nodes, risks, rows, cols):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = (0, 0)
    goal = (rows-1, cols-1)
    current_risk = 0
    unvisited[current] = current_risk

    while True:
        for neighbor, risk in risks[current].items():
            print(neighbor, risk)
            if neighbor not in unvisited:
                continue
            new_risk = current_risk + risk

            if unvisited[neighbor] is None or unvisited[neighbor] > new_risk:
                unvisited[neighbor] = new_risk

        visited[current] = current_risk
        del unvisited[current]

        if not unvisited:
            break

        candidates = [node for node in unvisited.items() if node[1]]
        current, current_risk = sorted(candidates, key=lambda x: x[1])[0]

    return visited[goal]


nodes1 = create_nodes(rows1, cols1)
risks1 = define_risks(rows1, cols1, lines)

# map2 = create_larger_map()
# rows2 = len(map2)
# cols2 = len(map2[0])
# nodes2 = create_nodes(rows2, cols2)
# risks2 = define_risks(rows2, cols2, map2)

answer1 = dijkstra(nodes1, risks1, rows1, cols1)
# answer2 = dijkstra(nodes2, risks2, rows2, cols2)
print(answer1)
