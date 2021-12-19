from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    rows1 = len(lines)
    cols1 = len(lines[0])


def find_neighbors(x, y, rows, cols):
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


def define_risks(rows, cols):
    risks = defaultdict()
    for x in range(rows):
        for y in range(cols):
            risks[(x, y)] = find_neighbors(x, y, rows, cols)
    return risks


def create_nodes(rows, cols):
    nodes = []
    for x in range(rows):
        for y in range(cols):
            nodes.append((x, y))
    return nodes


nodes1 = create_nodes(rows1, cols1)
risks1 = define_risks(rows1, cols1)


def dijkstra(nodes, risks):
    unvisited = {node: None for node in nodes}
    visited = {}
    current = (0, 0)
    currentRisk = 0
    unvisited[current] = currentRisk

    while True:
        for neighbour, risk in risks[current].items():
            if neighbour not in unvisited:
                continue
            newRisk = currentRisk + risk
            if unvisited[neighbour] is None or unvisited[neighbour] > newRisk:
                unvisited[neighbour] = newRisk
        visited[current] = currentRisk
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentRisk = sorted(candidates, key=lambda x: x[1])[0]
    return visited[(rows-1, cols-1)]


answer1 = dijkstra(nodes1, risks1)
print(answer1)
