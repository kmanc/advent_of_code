with open("in.txt", "r") as f:
  lines = [int(line.strip()) for line in f.readlines()]

new_lines = [sum(lines[i: i + 3]) for i in range(len(lines) - 2)]
count = len([index for index in range(1, len(new_lines)) if new_lines[index] > new_lines[index - 1]])

print(count)
