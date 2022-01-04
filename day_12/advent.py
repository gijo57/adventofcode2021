from collections import defaultdict
import heapq

with open('input.txt', 'r') as f:
    connections = [x.split('-') for x in f.read().split('\n')]
    vertices = defaultdict()

    for c in connections:
        vertices[c[0]] = []
        vertices[c[1]] = []
    for c in connections:
        vertices[c[0]].append(c[1])
        vertices[c[1]].append(c[0])


def search_paths():
    paths = []
    queue = [['start']]

    while queue:
        path = heapq.heappop(queue)
        last_vertex = path[-1]
        if last_vertex == 'end':
            paths.append(path)
        else:
            small_caves = [c for c in path if c.islower()]
            if(len(set(small_caves)) != len(small_caves)):
                continue
            neighbors = vertices[last_vertex]
            for n in neighbors:
                new_path = path[:]
                new_path.append(n)
                heapq.heappush(queue, new_path)
    return len(paths)


answer1 = search_paths()
print(answer1)
