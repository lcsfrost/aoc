import os
import re

Y = '2021'
D = '04'

"""
Quick notes and problem description:


Giant Squid wants to play bingo?

5x5 grid; chosen number is marked on all boards on which it appears
if all number sin any row or column are marked, the board wins

Instructions are in first row

Boards are below. 
"""



def solve_part_two():
    l = process_file()
    instruction_list = parse_instructions(l)
    board_dict = get_boards(l)
    scores_list = []
    for instruction in instruction_list:
        i = 1
        while i <= 100:
            if len(board_dict) == 0:
                return scores_list[-1]
            board = board_dict.get(i, None)
            if board is not None:
                if board.check_number(instruction):
                    print(f"board number {i} solved")
                    score = board_dict[i].score_board() * int(instruction)
                    scores_list.append(score)
                    board_dict.pop(i)
            i += 1
                

def solve_part_one():
    l = process_file()
    instruction_list = parse_instructions(l)
    board_dict = get_boards(l)
    for instruction in instruction_list:
        for board in board_dict.values():
            if board.check_number(instruction):
                return board.score_board() * int(instruction)


def get_boards(l):
    i = 1
    board_count = 1
    d = {}
    board_list = []
    while i < len(l):
        if l[i] == '':
            rows = l[i+1:i+6]
            d[board_count] = board(rows)
            board_count += 1
        i += 1
    return d



class board():
    def __init__(self, rows) -> None:
        self.d = {}
        for i, row in enumerate(rows):
            for j, val in enumerate(re.findall(r"\d+", row)):
                self.d[val] = (i,j)
        self.checked_grid = [[False for _ in range(5)] for _ in range(5)]

    def check_number(self, num):
        pos = self.d.pop(num, None)
        if pos is not None:
            self._mark_checked(pos)
            return self._check_solved(pos)

    def _mark_checked(self, pos):
        # print(pos)
        self.checked_grid[pos[0]][pos[1]] = True

    def _check_solved(self, pos):
        i, j = pos[0], pos[1]
        row_check = all([x for x in self.checked_grid[i]])
        col_check = all([x[j] for x in self.checked_grid])
        return any([row_check, col_check])
    
    def score_board(self):
        print(self.checked_grid)
        return sum([int(x) for x in self.d.keys()])
        # return sum(self.d.keys())


def parse_instructions(l:list):
    return [x.strip() for x in l[0].split(',')]

def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            l.append(line.strip())
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()