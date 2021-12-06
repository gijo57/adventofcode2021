from collections import Counter
import numpy as np

with open('input.txt', 'r') as f:
    vents = f.read().split('\n')


def count_intersections(vents):
    points = []
    for vent in vents:
        start, end = [[int(p) for p in x.strip().split(',')] for x in vent.split('->')]
        if (start[0] == end[0] or start[1] == end[1]):
            x = [start[0], end[0]]
            y = [start[1], end[1]]
            for i in range(min(x), max(x) + 1):
                for j in range(min(y), max(y) + 1):
                    points.append((i, j))
    return len([x for x in Counter(points).values() if x > 1])


def count_intersections2(vents):
    points = []
    for vent in vents:
        start, end = [[int(p) for p in x.strip().split(',')] for x in vent.split('->')]
        x = [start[0], end[0]]
        y = [start[1], end[1]]
        if (start[0] == end[0] or start[1] == end[1]):
            x = [start[0], end[0]]
            y = [start[1], end[1]]
            for i in range(min(x), max(x) + 1):
                for j in range(min(y), max(y) + 1):
                    points.append((i, j))
        else:
            length = abs(x[0] - x[1])
            if (x[0] > x[1]):
                for i in range(length + 1):
                    if (y[0] > y[1]):
                        points.append((x[0] - i, y[0] - i))
                    else:
                        points.append((x[0] - i, y[0] + i))                        
            else:
                for i in range(length + 1):
                    if (y[0] > y[1]):
                        points.append((x[0] + i, y[0] - i))
                    else:
                        points.append((x[0] + i, y[0] + i))
    return len([x for x in Counter(points).values() if x > 1])


answer1 = count_intersections(vents)
answer2 = count_intersections2(vents)
print(answer1, answer2)
