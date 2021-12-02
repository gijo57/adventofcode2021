def get_submarine_position():
    depth, position = 0, 0
    with open('input.txt', 'r') as f:
        for line in f:
            instruction = (line.split()[0], int(line.split()[1]))
            if (instruction[0] == 'up'):
                depth -= instruction[1]
            elif (instruction[0] == 'down'):
                depth += instruction[1]
            elif (instruction[0] == 'forward'):
                position += instruction[1]
    return depth * position


def get_improved_position():
    aim, depth, position = 0, 0, 0
    with open('input.txt', 'r') as f:
        for line in f:
            instruction = (line.split()[0], int(line.split()[1]))
            if (instruction[0] == 'up'):
                aim -= instruction[1]
            elif (instruction[0] == 'down'):
                aim += instruction[1]
            elif (instruction[0] == 'forward'):
                position += instruction[1]
                depth += aim * instruction[1]
    return depth * position


answer1 = get_submarine_position()
answer2 = get_improved_position()
print(answer1, answer2)
