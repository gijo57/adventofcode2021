with open('input.txt', 'r') as f:
    positions = [int(x) for x in f.read().split(',')]


def get_fuel_cost(positions, aligned_position):
    fuel_cost = 0
    for p in positions:
        distance = abs(p - aligned_position)
        fuel_cost += distance
    return fuel_cost


def get_advanced_fuel_cost(positions, aligned_position):
    fuel_cost = 0
    for p in positions:
        distance = abs(p - aligned_position)
        fuel_cost += int(distance * (distance + 1) / 2)
    return fuel_cost


def get_lowest_cost(positions, fn):
    lowest_cost = fn(positions, 1)
    for i in range(min(positions), max(positions) + 1):
        cost = fn(positions, i)
        if cost < lowest_cost:
            lowest_cost = cost
    return lowest_cost


answer1 = get_lowest_cost(positions, get_fuel_cost)
answer2 = get_lowest_cost(positions, get_advanced_fuel_cost)
print(answer1, answer2)
