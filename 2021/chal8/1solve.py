with open("in.txt", "r") as f:
    lines = [line for line in f.readlines()]
    lines = [(line.split("|")[0].strip(), line.split("|")[1].strip()) for line in lines]

total = 0
for line in lines:
    real_string = line[1]
    reals = real_string.split(" ")
    for real in reals:
        if len(real) in (2, 3, 4, 7):
            total += 1

print(total)
