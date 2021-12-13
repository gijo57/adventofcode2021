import numpy as np

with open('input.txt', 'r') as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    rows = len(lines)
    cols = len(lines[0])
    total_octopi = rows*cols


def find_neighbors(x, y):
    neighbors = []
    x_vals = [-1, 0, +1]
    y_vals = [-1, 0, +1]
    for x2 in x_vals:
        for y2 in y_vals:
            if (y + y2 >= 0 and x + x2 >= 0 and y + y2 < cols and x + x2 < rows):
                if (x, y) != (x + x2, y + y2):
                    neighbors.append((x + x2, y + y2))
    return neighbors


def handle_flashes(coords, flashed):
    updates = []
    flashed_octopi = flashed

    for x, y in coords:
        if (lines[x][y] > 9 and (x, y) not in flashed_octopi):
            flashed_octopi.append((x, y))
            neighbors = find_neighbors(x, y)
            updates.extend(neighbors)
    for u in updates:
        lines[u[0]][u[1]] += 1
    flashing_coords = []
    for x, y in coords:
        if (lines[x][y] > 9 and (x, y) not in flashed_octopi):
            flashing_coords.append((x, y))
    if flashing_coords:
        return handle_flashes(coords, flashed_octopi)
    else:
        for x, y in flashed_octopi:
            lines[x][y] = 0
        return len(flashed_octopi)


def run_step():
    coords = []
    for x in range(rows):
        for y in range(cols):
            coords.append((x, y))
            lines[x][y] += 1
    new_flashes = handle_flashes(coords, [])
    return new_flashes


def simulate_steps(steps):
    synchronized_step = 0
    flashes = 0
    for i in range(steps):
        new_flashes = run_step()
        print(new_flashes)
        flashes += new_flashes
    return flashes


answer1 = simulate_steps(100)
print(answer1)