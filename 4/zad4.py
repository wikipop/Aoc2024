import numpy as np

with open("input.txt") as f:
    lines = np.array([list(word.strip()) for word in f.readlines()])
    S = 0

    for iteration in range(4):
        for i in range(-len(lines), len(lines)):
            line = lines.diagonal(i)
            S += np.sum([np.all(line[i:i + 4] == np.array(list("XMAS"))) for i in range(len(line) - 3)])

        for line in lines:
            S += np.sum([np.all(line[i:i+4] == np.array(list("XMAS"))) for i in range(len(line) - 3)])

        lines = np.rot90(lines)

    print(S)

with open("input.txt") as f:
    lines = np.array([list(word.strip()) for word in f.readlines()])
    S = 0

    for i in range(len(lines)-2):
        for j in range(len(lines)-2):
            diag1 = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2]
            diag2 = lines[i + 2][j] + lines[i + 1][j + 1] + lines[i][j + 2]
            if diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}:
                S += 1

    print(S)