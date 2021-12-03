with open('index.txt', 'r') as f:
    values = [v.strip() for v in f.readlines()]
    val_length = len(values[0])


def get_counts(input, val_length):
    counts = [[0 for y in range(2)] for x in range(val_length)]

    for value in input:
        for i, digit in enumerate(value):
            counts[i][int(digit)] += 1
    return counts


def get_pwr_consumption(input, val_length):
    counts = get_counts(input, val_length)

    gamma = int(''.join([str(counts[i].index(max(x))) for i, x in enumerate(counts)]), 2)
    epsilon = int(''.join([str(counts[i].index(min(x))) for i, x in enumerate(counts)]), 2)
    return gamma * epsilon


def get_life_support_rating(oxygen_input, co2_input, oxygen_start, co2_start):
    print('ox', oxygen_input, len(oxygen_input), oxygen_start)
    print('co', co2_input, len(co2_input), co2_start)

    oxygen_counts, co2_counts = [0, 0], [0, 0]
    for input in oxygen_input:
        oxygen_counts[int(input[oxygen_start])] += 1
    for input in co2_input:
        co2_counts[int(input[co2_start])] += 1

    most_common_oxygen_bit = str(oxygen_counts.index(max(oxygen_counts)))
    least_common_co2_bit = str(co2_counts.index(min(co2_counts)))

    oxygen_values = [x for x in oxygen_input if x[oxygen_start] == most_common_oxygen_bit]
    co2_values = [x for x in co2_input if x[co2_start] == least_common_co2_bit]

    if (len(oxygen_values) == 1 and len(co2_values) == 1): 
        return oxygen_values, co2_values
    else:
        return get_life_support_rating(oxygen_values, co2_values, oxygen_start + 1, co2_start + 1)


answer1 = get_pwr_consumption(values, val_length)
answer2 = get_life_support_rating(values, values, 0, 0)
print(answer1, answer2)
