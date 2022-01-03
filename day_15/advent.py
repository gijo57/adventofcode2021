from collections import defaultdict
from copy import deepcopy
import numpy as np
from math import inf
import heapq

with open('input.txt', 'r') as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]


def create_graph(rows, cols, data):
    graph = defaultdict()
    x_vals = [-1, 0, +1]
    y_vals = [-1, 0, +1]

    for x in range(rows):
        for y in range(cols):
            vertex = defaultdict()
            for x2 in x_vals:
                for y2 in y_vals:
                    if (y + y2 >= 0 and x + x2 >= 0 and y + y2 < cols and x + x2 < rows):
                        if (x, y) != (x + x2, y + y2):
                            if (x2 == 0 or y2 == 0):
                                vertex[(x + x2, y + y2)] = (data[x + x2][y + y2])
            graph[(x, y)] = vertex
    return graph


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


def dijkstra(graph, starting_vertex, goal):
    distances = {vertex: inf for vertex in graph}
    distances[starting_vertex] = 0

    queue = [(0, starting_vertex)]
    while len(queue) > 0:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances[goal]


rows1 = len(lines)
cols1 = len(lines[0])
graph = create_graph(rows1, cols1, lines)

lines2 = create_larger_map()
rows2 = len(lines2)
cols2 = len(lines2[0])
graph2 = create_graph(rows2, cols2, lines2)

answer1 = dijkstra(graph, (0, 0), (rows1-1, cols1-1))
answer2 = dijkstra(graph2, (0, 0), (rows2-1, cols2-1))
print(answer1, answer2)
