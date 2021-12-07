with open("in.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

mover = {"down": 1, "up": -1}
xpos = 0
ypos = 0
for line in lines:
  amount = int(line.split(" ")[1])
  multiplier = mover.get(line.split(" ")[0])
  if multiplier:
    ypos += amount * multiplier
  else:
    xpos += amount

print(xpos*ypos)
