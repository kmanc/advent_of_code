from collections import Counter
import operator

with open("in.txt", "r") as f:
    fishies = [int(fish) for fish in f.read().strip().split(',')]

fishies = Counter(fishies)
for day in range(80):
    new_sevens = fishies.get(8, 0)
    new_sixes = fishies.get(7, 0)
    fishies = Counter({(fish - 1) % 7: value for fish, value in fishies.items() if fish <= 6})
    new_eights = fishies.get(6, 0)
    fishies[8] = new_eights
    fishies[7] = new_sevens
    fishies[6] += new_sixes

print(sum(fishies.values()))

