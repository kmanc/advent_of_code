import numpy as np
import operator

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

matrix = np.zeros((len(lines), len(lines[0])))
num_rows, num_cols = matrix.shape
ones = np.ones((len(lines), len(lines[0])))

for row, line in enumerate(lines):
    for column, char in enumerate(line):
        matrix[row][column] = char

left = (0, -1)
up = (-1, 0)
right = (0, 1)
down = (1, 0)
d_up_left = (-1, 1)
d_up_right = (1, 1)
d_down_right = (1, -1)
d_down_left = (-1, -1)
directions = [left, right, up, down, d_up_left, d_up_right, d_down_right, d_down_left]

def iterative_flood_fill(in_matrix, indicies):
    seen = set()
    while len(indicies) > 0:
        current_index = indicies.pop()
        if current_index in seen:
            continue
        seen.add(current_index)
        for dir in directions:
            new_row, new_col = (current_index[0] + dir[0], current_index[1] + dir[1])
            if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                continue
            matrix[new_row][new_col] += 1
            if matrix[new_row][new_col] > 9 and (new_row, new_col) not in seen:
                indicies.append((new_row, new_col))

    return len(seen)

flashes = 0
for loop in range(100):
    matrix = matrix + ones
    nines = np.where(matrix > 9)
    nines = [(row, col) for row, col in zip(nines[0], nines[1])]
    flashes += iterative_flood_fill(matrix, nines)
    nine_or_mores = np.where(matrix > 9)
    nine_or_mores = [(row, col) for row, col in zip(nine_or_mores[0], nine_or_mores[1])]
    for nine_or_more in nine_or_mores:
        matrix[nine_or_more[0]][nine_or_more[1]] = 0

print(flashes)
