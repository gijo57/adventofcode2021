with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    numbers = [int(n) for n in parts[0].split(',')]

    tables = parts[1:]
    tables = [[[int(x) for x in row.split()] for row in t.split('\n')] for t in tables]


def get_score(numbers, table):
    steps = 0
    for number in numbers:
        for row in table:
            if number in row:
                row[row.index(number)] = True
            if all(x == True for x in row):
                filtered_table = list(filter(lambda x: not isinstance(x, bool), [n for sublist in table for n in sublist]))
                return sum(filtered_table) * number, steps
            for i in range(len(table[0])):
                column = [row[i] for row in table]
                if all(x == True for x in column):
                    filtered_table = list(filter(lambda x: not isinstance(x, bool), [n for sublist in table for n in sublist]))
                    return sum(filtered_table) * number, steps
        steps += 1


def solve(numbers, tables):
    results = []
    for table in tables:
        results.append(get_score(numbers, table))
    return results

results = solve(numbers, tables)
answer_1 = min(results, key = lambda x: x[1])[0]
answer_2 = max(results, key = lambda x: x[1])[0]
print(answer_1, answer_2)
