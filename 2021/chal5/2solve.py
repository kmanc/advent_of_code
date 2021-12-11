import numpy as np
import sys

with open("in.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

lines = [line.split("->") for line in lines]
lines = [(line[0].strip(), line[1].strip()) for line in lines]
lines = [((int(line[0].split(",")[0]), int(line[0].split(",")[1])), (int(line[1].split(",")[0]), int(line[1].split(",")[1]))) for line in lines]
rows = [(line[0][1], range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1)) for line in lines if line[0][1] == line[1][1]]
columns = [(line[0][0], range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1)) for line in lines if line[0][0] == line[1][0]]
diagonals = [(line[0][0], line[0][1], line[1][0], line[1][1]) for line in lines if abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1])]

matrix = np.zeros((1000, 1000))
for row in rows:
    row_index, column_range = row
    for col_val in column_range:
        matrix[row_index][col_val] += 1
for column in columns:
    column_index, row_range = column
    for row_val in row_range:
        matrix[row_val][column_index] += 1
for diagonal in diagonals:
    first_x, first_y, second_x, second_y = diagonal
    range_len = abs(first_x - second_x) + 1
    if first_x > second_x and first_y > second_y:
        for index in range(range_len):
            matrix[second_y + index][second_x + index] += 1
    elif first_x > second_x and first_y < second_y:
        for index in range(range_len):
            matrix[second_y - index][second_x + index] += 1
    elif first_x < second_x and first_y > second_y:
        for index in range(range_len):
            matrix[second_y + index][second_x - index] += 1
    else:
        for index in range(range_len):
            matrix[second_y - index][second_x - index] += 1

print(len(matrix[matrix >= 2]))
