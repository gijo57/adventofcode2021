from statistics import median

with open('index.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]

opening_chars = ["{", "(", "[", "<"]
pairs = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">"
}
scores = {
    "}": 1197,
    ")": 3,
    "]": 57,
    ">": 25137
}

incomplete_lines = lines[:]


def get_score():
    score = 0

    for line in lines:
        stack = []
        for char in line:
            if (char in opening_chars):
                stack.append(char)
            else:
                opening_char = stack.pop()
                if (char != pairs[opening_char]):
                    incomplete_lines.pop(incomplete_lines.index(line))
                    score += scores[char]
                    break
    return score


scores2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def get_completion_score(line):
    score = 0
    stack = []
    for char in line:
        if (char in opening_chars):
            stack.append(char)
        else:
            stack.pop()

    for char in reversed(stack):
        score = score * 5 + scores2[char]
    return score


def get_score2():
    completion_scores = []
    for line in incomplete_lines:
        completion_scores.append(get_completion_score(line))
    return median(completion_scores)


answer1 = get_score()
answer2 = get_score2()
print(answer1, answer2)
