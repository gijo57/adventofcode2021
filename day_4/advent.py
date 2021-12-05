with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    numbers = [int(n) for n in parts[0].split(',')]

    tables = parts[1:]
    tables = [[[int(x) for x in row.split()] for row in t.split('\n')] for t in tables]


def solve_1(numbers, tables):
    for number in numbers:
        for table in tables:
            for i in range(len(table[0])):
                column = [row[i] for row in table]
                if all(x == True for x in column):
                    filtered_table = list(filter(lambda x: not isinstance(x, bool), [n for sublist in table for n in sublist]))
                    return sum(filtered_table) * number
            for row in table:
                if number in row:
                    row[row.index(number)] = True
                if all(x == True for x in row):
                    filtered_table = list(filter(lambda x: not isinstance(x, bool), [n for sublist in table for n in sublist]))
                    return sum(filtered_table) * number


def solve_2(numbers, tables):



answer_1 = solve_1(numbers, tables)
answer_2 = solve_2(numbers, tables)
print(answer_1, answer_2)
