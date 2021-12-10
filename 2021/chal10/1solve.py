from collections import deque

with open("in.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

close_to_open = {
")": "(",
"]": "[",
"}": "{",
">": "<"
}

char_to_score = {
")": 3,
"]": 57,
"}": 1197,
">": 25137
}

score = 0
for line in lines:
    openers = deque()
    for char in line:
        if char in close_to_open.values():
            openers.append(char)
        else:
            if close_to_open[char] != openers.pop():
                score += char_to_score[char]

print(score)
