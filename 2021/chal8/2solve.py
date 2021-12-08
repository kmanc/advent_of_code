from collections import Counter
import operator

with open("in.txt", "r") as f:
    lines = [line for line in f.readlines()]
    lines = [(line.split("|")[0].strip(), line.split("|")[1].strip()) for line in lines]

letters_numbers_dict = {
"abcefg": 0,
"cf": 1,
"acdeg": 2,
"acdfg": 3,
"bcdf": 4,
"abdfg": 5,
"abdefg": 6,
"acf": 7,
"abcdefg": 8,
"abcdfg": 9
}

total = 0
for line in lines:
    scramble_unscramble_dict = {}

    seed_string = line[0]

    b_map = {letter for letter in seed_string if seed_string.count(letter) == 6 and letter != " "}.pop()
    scramble_unscramble_dict[b_map] = "b"

    e_map = {letter for letter in seed_string if seed_string.count(letter) == 4 and letter != " "}.pop()
    scramble_unscramble_dict[e_map] = "e"

    f_map = {letter for letter in seed_string if seed_string.count(letter) == 9 and letter != " "}.pop()
    scramble_unscramble_dict[f_map] = "f"

    seeds = sorted(seed_string.split(" "), key=len)

    c_map = seeds[0].replace(f_map, "")
    scramble_unscramble_dict[c_map] = "c"

    a_map = seeds[1].replace(c_map, "").replace(f_map, '')
    scramble_unscramble_dict[a_map] = "a"

    six_len = "".join(entry for entry in seeds if len(entry) == 6)
    six_len = "".join(letter for letter in six_len if letter not in scramble_unscramble_dict)
    g_map = {letter for letter in seed_string if six_len.count(letter) == 3}.pop()
    scramble_unscramble_dict[g_map] = "g"

    d_map = {letter for letter in seed_string if six_len.count(letter) == 2}.pop()
    scramble_unscramble_dict[d_map] = "d"

    real_values = line[1].split(" ")
    mini_total = 0
    for real_value in real_values:
        real_chars = "".join(sorted([scramble_unscramble_dict[val] for val in real_value]))
        mini_total *= 10
        mini_total += letters_numbers_dict[real_chars]

    total += int(mini_total)

print(total)
