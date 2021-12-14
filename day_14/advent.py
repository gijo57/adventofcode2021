from collections import Counter

with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    template = parts[0]
    rule_list = [x.split('->') for x in parts[1].split('\n')]
    rules = {}
    for r in rule_list:
        rules[r[0].strip()] = r[1].strip()


def run_step(polymer):
    updated_polymer = []
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append(polymer[i] + polymer[i+1])

    for i, pair in enumerate(pairs):
        new_element = rules[pair]
        if (i == 0):
            updated_polymer.append(pair[0] + new_element + pair[1])
        else:
            updated_polymer.append(new_element + pair[1])
    return ''.join(updated_polymer)


def run_steps(steps):
    polymer = template

    for i in range(steps):
        polymer = run_step(polymer)
    return polymer


final_polymer = run_steps(10)
most_common = Counter(final_polymer).most_common(1)[0][1]
least_common = min(Counter(final_polymer).values())
answer1 = most_common - least_common
print(answer1)
