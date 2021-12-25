import numpy as np

with open('input.txt', 'r') as f:
    seafloor = np.array([list(x.strip()) for x in f.readlines()])


def move_east_facing(east_facing):
    moved_count = 0
    for cucumber in east_facing:
        seafloor[cucumber[0]][cucumber[1]] = '.'
        if (cucumber[1] + 1 == len(seafloor[0])):
            seafloor[cucumber[0]][0] = '>'
        else:
            seafloor[cucumber[0]][cucumber[1] + 1] = '>'
        moved_count += 1
    return moved_count


def move_south_facing(south_facing):
    moved_count = 0
    for cucumber in south_facing:
        seafloor[cucumber[0]][cucumber[1]] = '.'
        if (cucumber[0] + 1 == len(seafloor)):
            seafloor[0][cucumber[1]] = 'v'
        else:
            seafloor[cucumber[0] + 1][cucumber[1]] = 'v'
        moved_count += 1
    return moved_count


def can_move(i, j):
    if (seafloor[i][j] == '>'):
        if (j+1 == len(seafloor[0])):
            if (seafloor[i][0] == '.'):
                return 'East'
        else:
            if (seafloor[i][j+1] == '.'):
                return 'East'
    elif (seafloor[i][j] == 'v'):
        if (i+1 == len(seafloor)):
            if (seafloor[0][j] == '.'):
                return 'South'
        else:
            if (seafloor[i+1][j] == '.'):
                return 'South'
    return False


def simulate_step():
    move_east = []
    move_south = []
    moved_count = 0
    for i in range(len(seafloor)):
        for j in range(len(seafloor[0])):
            if (can_move(i, j) == 'East'):
                move_east.append((i, j))
    moved_count += move_east_facing(move_east)
    for i in range(len(seafloor)):
        for j in range(len(seafloor[0])):
            if (can_move(i, j) == 'South'):
                move_south.append((i, j))
    moved_count += move_south_facing(move_south)
    return moved_count > 0


def simulate(moves):
    moved = simulate_step()
    if (moved):
        return simulate(moves+1)
    else:
        return moves+1


print(simulate(0))
