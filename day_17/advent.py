import re

with open('input.txt', 'r') as f:
    target_values = [int(x) for x in re.findall('(-\d*|\d*)', f.read()) if x != '']
    x_bounds = target_values[:2]
    y_bounds = target_values[2:]


def run_step(velocity, location):
    new_location = (location[0] + velocity[0], location[1] + velocity[1])
    new_x_velocity = velocity[0] - 1 if velocity[0] > 0 else velocity[0] + 1 if velocity[0] < 0 else 0
    new_velocity = (new_x_velocity, velocity[1] - 1)
    return new_velocity, new_location


def launch(init_velocity):
    current_position = (0, 0)
    current_velocity = init_velocity
    highest_y = current_position[1]

    while (current_position[1] >= min(y_bounds)):
        current_velocity, current_position = run_step(current_velocity, current_position)
        if (current_position[1] > highest_y):
            highest_y = current_position[1]
        legit_x = current_position[0] >= x_bounds[0] and current_position[0] <= x_bounds[1]
        legit_y = current_position[1] >= y_bounds[0] and current_position[1] <= y_bounds[1]

        if (legit_x and legit_y):
            return highest_y


def find_init_velocity():
    highest_y = 0
    for i in range(0, 300):
        for j in range(0, 300):
            y = launch((i, j))
            if (y):
                if (y > highest_y):
                    highest_y = y
    return highest_y


answer1 = find_init_velocity()
print(answer1)
