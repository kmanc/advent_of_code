import itertools
import copy

with open("in.txt", "r") as f:
  lines = [line.strip() for line in f.readlines()]

called_nums = lines[0].split(",")

def create_board(list_of_five_lines):
    board = {}
    for i in range(5):
        board[i] = list_of_five_lines[i]
    for i in range(5):
        board[i+5] = [line[i] for line in list_of_five_lines]

    return board

undone_boards = [line.strip() for line in lines[1:] if line.strip()]
boards = []
for i in range(int(len(undone_boards) / 5)):
    fives = [line.split() for line in undone_boards[(i*5):(i*5)+5]]
    new_board = create_board(fives)
    boards.append(new_board)

winners = []
added = []
for called_num in called_nums:
    for board_num, board in enumerate(boards):
        for k, v in board.items():
            try:
                v.remove(called_num)
            except ValueError:
                pass
            if not v and board_num not in added:
                board[k] = v
                winners.append((copy.deepcopy(board), called_num))
                added.append(board_num)
            board[k] = v

last_win = winners[-1]
board = last_win[0]
called_num =  last_win[1]
remaining = set(itertools.chain.from_iterable(a for a in board.values() if a))
points = sum((int(num) for num in remaining))
print(points * int(called_num))
