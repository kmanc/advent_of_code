with open("in.txt", "r") as f:
  lines = [int(line.strip()) for line in f.readlines()]

count = len([index for index in range(1, len(lines)) if lines[index] > lines[index - 1]])

print(count)
