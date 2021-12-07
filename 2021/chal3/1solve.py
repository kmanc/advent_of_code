import operator

with open("in.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

halfway = len(lines) / 2
length = len(lines[0])
ones = [operator.countOf((line[index] for line in lines),"1") for index in range(length)]
gamma = ''.join((str(int(val>halfway)) for val in ones))
epsilon = ''.join((str(int(val<halfway)) for val in ones))

print(int(gamma, 2) * int(epsilon, 2))
