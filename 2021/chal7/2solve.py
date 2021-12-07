from collections import Counter
import operator

with open("in.txt", "r") as f:
    positions = [int(pos) for pos in f.read().strip().split(',')]

smallest = min(positions)
largest = max(positions)
costs = {}
for index in range(smallest, largest + 1):
    cost = [abs(position - index) for position in positions]
    costs[index] = sum([sum(range(step+1)) for step in cost])

print(min(costs.values()))

