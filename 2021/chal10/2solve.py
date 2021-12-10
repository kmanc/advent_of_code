from collections import deque

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

close_to_open = {
")": "(",
"]": "[",
"}": "{",
">": "<"
}

open_to_close = {v: k for k, v in close_to_open.items()}

char_to_score = {
")": 1,
"]": 2,
"}": 3,
">": 4
}

scores = []
for line in lines:
    score = 0
    openers = deque()
    for char in line:
        if char in close_to_open.values():
            openers.append(char)
        else:
            if close_to_open[char] != openers.pop():
                openers = deque()
                break
    if openers:
        openers.reverse()
        closers = "".join(open_to_close[char] for char in openers)
        for char in closers:
            score *= 5
            score += char_to_score[char]
        scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])
