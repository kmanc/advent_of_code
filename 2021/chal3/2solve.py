import operator

with open("in.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

length = len(lines[0])

def reduce_list(index, oxygen, carbon):
    if index >= length:
        return oxygen, carbon

    print(f"Index: {index}, oxygen remaining --> {len(oxygen)}, carbon remaining --> {len(carbon)}")

    halfway_o2 = len(oxygen) / 2
    halfway_c02 = len(carbon) / 2
    ones_o2 = operator.countOf((line[index] for line in oxygen),"1")
    ones_c02 = operator.countOf((line[index] for line in carbon),"1")

    oxygen_pos = str(int(ones_o2>=halfway_o2))
    carbon_pos = str(int(ones_c02<halfway_c02))

    out_oxygen = [line for line in oxygen if oxygen_pos == line[index]]
    out_carbon = [line for line in carbon if carbon_pos == line[index]]

    if len(out_oxygen) > 1 or len(out_carbon) > 1:
        return reduce_list(index+1, out_oxygen or [oxygen[-1]], out_carbon or [carbon[-1]])

    return out_oxygen or [oxygen[-1]], out_carbon or [carbon[-1]]

oxygen, carbon = reduce_list(0, lines, lines)
print(int(oxygen[0], 2) * int(carbon[0], 2))
