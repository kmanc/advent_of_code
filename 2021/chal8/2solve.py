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
    # Seed inputs sorted shortest --> longest
    seeds = sorted(seed_string.split(" "), key=len)
    # Seed inputs as one long string without spaces
    seed_string = seed_string.replace(" ", "")

    # The letter b shows up in 6 of the displays
    b_map = {letter for letter in seed_string if seed_string.count(letter) == 6}.pop()
    scramble_unscramble_dict[b_map] = "b"

   # The letter e shows up in 4 of the displays
    e_map = {letter for letter in seed_string if seed_string.count(letter) == 4}.pop()
    scramble_unscramble_dict[e_map] = "e"

    # The letter f shows up in 9 of the displays
    f_map = {letter for letter in seed_string if seed_string.count(letter) == 9}.pop()
    scramble_unscramble_dict[f_map] = "f"

    # Since the shortest seed input has f + c and we already know f, we know c
    c_map = seeds[0].replace(f_map, "")
    scramble_unscramble_dict[c_map] = "c"

    # Like above, the second shortest input has f + c + a and we already know f + c
    a_map = seeds[1].replace(c_map, "").replace(f_map, '')
    scramble_unscramble_dict[a_map] = "a"

    # Of the unsolved letters left (d + g), g shows up 3 times in the seeds that have 6 segments
    six_len = "".join(entry for entry in seeds if len(entry) == 6)
    six_len = "".join(letter for letter in six_len if letter not in scramble_unscramble_dict)
    g_map = {letter for letter in seed_string if six_len.count(letter) == 3}.pop()
    scramble_unscramble_dict[g_map] = "g"

    # Like above, d shows up only twice in the seeds that have 6 segments
    d_map = {letter for letter in seed_string if six_len.count(letter) == 2}.pop()
    scramble_unscramble_dict[d_map] = "d"

    # Remap the scrambled letters to the correct ones, reconstruct the string and sort it alphabetically so I can map it to its real number via the dict outside this loop
    real_values = line[1].split(" ")
    mini_total = 0
    for real_value in real_values:
        real_chars = "".join(sorted([scramble_unscramble_dict[val] for val in real_value]))
        mini_total *= 10
        mini_total += letters_numbers_dict[real_chars]

    total += int(mini_total)

print(total)
