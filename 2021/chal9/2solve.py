import numpy as np
import operator

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

def find_new_mins(in_matrix):
    result = np.where(in_matrix == 0)
    candidates = ((row, col) for row, col in zip(result[0], result[1]))
    for candidate in candidates:
        if all(neighbor_is_positive(candidate, dir) for dir in directions):
            risk_vals.append(candidate)

def iterative_flood_fill(in_matrix, index):
    q = [index]
    seen = set()

    while len(q) > 0:
        current_index = q.pop()
        seen.add(current_index)
        for dir in directions:
            new_candidate = (current_index[0] + dir[0], current_index[1] + dir[1])
            if new_candidate[0] < 0 or new_candidate[1] < 0 or new_candidate in seen:
                continue
            if not neighbor_is_positive(current_index, dir):
                q.append(new_candidate)

    return len(seen)

for loop in range(8):
    find_new_mins(matrix)
    matrix = matrix + minus_ones

valley_sizes = [iterative_flood_fill(matrix, risk_val) for risk_val in risk_vals]
valley_sizes.sort()
print(valley_sizes[-3] * valley_sizes[-2] * valley_sizes[-1])
