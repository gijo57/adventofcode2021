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
                    score += scores[char]
                    break
    return score


answer1 = get_score()
print(answer1)
