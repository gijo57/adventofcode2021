import numpy as np

with open('input.txt', 'r') as f:
    parts = f.read().split('\n\n')
    dot_coords = [[int(y) for y in x.split(',')] for x in parts[0].split('\n')]
    folds = [x.split(' ')[-1] for x in parts[1].split('\n')]
    columns = max([x[0] for x in dot_coords])+1
    rows = max([x[1] for x in dot_coords])+1

paper = np.array([['.']*columns for i in range(rows)])


def create_paper():
    for point in dot_coords:
        paper[point[1]][point[0]] = '#'


def fold(fold_index, paper):
    fold = folds[fold_index].split('=')
    folding_point = int(fold[1])

    if (fold[0] == 'y'):
        above_fold = paper[:folding_point]
        below_fold = np.flip(paper[folding_point+1:], axis=0)

        if (len(above_fold) >= len(below_fold)):
            start_point = len(above_fold) - len(below_fold)
            for i in range(start_point, len(above_fold)):
                for j in range(len(above_fold[i])):
                    if (below_fold[i-start_point][j] == '#'):
                        above_fold[i][j] = '#'
            return above_fold, (above_fold == '#').sum()
        else:
            start_point = len(below_fold) - len(above_fold)
            for i in range(start_point, len(below_fold)):
                for j in range(len(below_fold[i])):
                    if (above_fold[i-start_point][j] == '#'):
                        below_fold[i][j] = '#'
            return below_fold, (below_fold == '#').sum()
    else:
        left = np.array([x[:folding_point] for x in paper])
        right = np.flip(np.array([x[folding_point+1:] for x in paper]), axis=1)

        if (len(left[0]) >= len(right[0])):
            start_point = len(left[0]) - len(right[0])
            for i in range(len(left)):
                for j in range(len(left[i])):
                    if (j >= start_point):
                        if (right[i][j-start_point] == '#'):
                            left[i][j] = '#'
            return left, (left == '#').sum()
        else:
            start_point = len(right[0]) - len(left[0])
            for i in range(len(right)):
                for j in range(len(right[i])):
                    if (j < len(right[i]) - start_point):
                        if (left[i][j] == '#'):
                            right[i][j] = '#'
            return right, (right == '#').sum()


def complete_folds(folds, paper):
    answer1 = 0
    paper = paper
    for i in range(len(folds)):
        paper = fold(i, paper)[0]
        if (i == 0):
            answer1 = fold(i, paper)[1]
    return answer1, paper


create_paper()
answer1, answer2 = complete_folds(folds, paper)
print(answer1)
print(answer2)
