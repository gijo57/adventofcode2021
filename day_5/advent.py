from collections import Counter

with open('input.txt', 'r') as f:
    vents = f.read().split('\n')


def draw_vents(vents):
    points = []
    for vent in vents:
        start, end = [[int(p) for p in x.strip().split(',')] for x in vent.split('->')]
        if (start[0] == end[0] or start[1] == end[1]):
            x = [start[0], end[0]]
            y = [start[1], end[1]]
            for i in range(min(x), max(x) + 1):
                for j in range(min(y), max(y) +1):
                    points.append((i, j))
    return len([x for x in Counter(points).values() if x > 1])


answer1 = draw_vents(vents)
print(answer1)