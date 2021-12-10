import numpy as np

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

matrix = np.zeros((len(lines), len(lines[0])))
minus_ones = np.full((len(lines), len(lines[0])), -1)

for row, line in enumerate(lines):
    for column, char in enumerate(line):
        matrix[row][column] = char

risk_vals = []
left = (0, -1)
up = (-1, 0)
right = (0, 1)
down = (1, 0)
directions = [left, right, up, down]

def neighbor_is_positive(index, direction):
    row, col = index
    row_add, column_add = direction
    try:
        return matrix[row + row_add][col + column_add] > 0
    except IndexError:
        return True

def find_new_mins(in_matrix,  iteration):
    result = np.where(in_matrix == 0)
    candidates = ((row, col) for row, col in zip(result[0], result[1]))
    for candidate in candidates:
        if all(neighbor_is_positive(candidate, dir) for dir in directions):
            risk_vals.append(iteration)

for loop in range(9):
    find_new_mins(matrix, loop)
    matrix = matrix + minus_ones

print(sum(risk_vals) + len(risk_vals))
