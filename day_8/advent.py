with open('input.txt', 'r') as f:
    lines = f.readlines()
    outputs = [x.split('|')[1].split() for x in lines]
    digits = [item for sublist in outputs for item in sublist]


def solve1(digits):
    return len([x for x in digits if len(x) in [2, 3, 4, 7]])


def solve2(lines):
    result = 0
    digits = {
        '1': '',
        '2': '',
        '3': '',
        '4': '',
        '5': '',
        '6': '',
        '7': '',
        '8': '',
        '9': '',
        '0': '',
    }

    for line in lines:
        output = ''
        signal_pattern = line.split('|')[0]
        signal_digits = [x for x in signal_pattern.split()]

        for d in signal_digits:
            if len(d) == 2:
                digits['1'] = ''.join(sorted(d))
            elif len(d) == 3:
                digits['7'] = ''.join(sorted(d))
            elif len(d) == 4:
                digits['4'] = ''.join(sorted(d))
            elif len(d) == 7:
                digits['8'] = ''.join(sorted(d))

        for d in signal_digits:
            if len(d) == 6:
                if (all(c in d for c in digits['4'])):
                    digits['9'] = ''.join(sorted(d))
                elif (all(c in d for c in digits['1'])):
                    digits['0'] = ''.join(sorted(d))
                else:
                    digits['6'] = ''.join(sorted(d))

        for d in signal_digits:
            if len(d) == 5:
                if (all(c in d for c in digits['1'])):
                    digits['3'] = ''.join(sorted(d))
                elif (all(c in digits['6'] for c in d)):
                    digits['5'] = ''.join(sorted(d))
                else:
                    digits['2'] = ''.join(sorted(d))
        output_digits = line.split('|')[1].strip().split(' ')
        for digit in output_digits:
            output += list(digits.keys())[list(digits.values()).index(''.join(sorted(digit)))]
        result += int(output)
    return result

answer1 = solve1(digits)
answer2 = solve2(lines)
print(answer1, answer2)
