import re
import numpy as np

with open('input.txt', 'r') as f:
    rows = [re.findall('(on|off)|(-*\d+..-*\d+)', x) for x in f.readlines()]
    limits = []
    reactor_state = np.zeros([100, 100, 100])

    for row in rows:
        limit = []
        status = row[0][0]
        limit.append(status)
        for i in range(1, 4):
            elem = row[i][1].split('..')
            limit.append([int(x)+50 for x in elem])
        limits.append(limit)

for limit in limits:
    handled_cubes = []
    cube_value = 1 if limit[0] == 'on' else 0
    for i in range(len(reactor_state)):
        for j in range(len(reactor_state[i])):
            for k in range(len(reactor_state[i][j])):
                if (i >= limit[1][0] and i <= limit[1][1] and j >= limit[2][0] and j <= limit[2][1] and k >= limit[3][0] and k <= limit[3][1]):
                    reactor_state[i][j][k] = cube_value

answer1 = np.sum(reactor_state)
print(answer1)
