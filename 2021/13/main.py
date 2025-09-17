import os

Y = '2021'
D = '13'

"""
Quick notes and problem description:

Transparent paper
instructions on how to fold it (input)

x, y
6, 10
0, 14
9,10

fold along y=7
fold along x=5

x increases to the right
y increases downwards

OKAY SO HERE WE GO:
create numpy matrix

np.fliplr to fold horizontally
np.flipud  to fold vertically
np.bitwise_or to find "matches"/dots/points/whatever

Needs:


"""



def solve_part_one():
    ans = ''
    return ans

def solve_part_two():
    ans = ''
    return ans






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

def testing():
    import re
    import math
    l = process_file()
    max_x = 0
    max_y = 0
    for line in l:
        if line:
            if 'fold' in line:
                1
            else:
                nums = re.findall(r"\d+", line)
                max_x = max(max_x, int(nums[0]))
                max_y = max(max_y, int(nums[1]))
    print(max_x, max_y)
    return

def main():
    testing()
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    # print(f"Part one answer: {part_one_ans}")
    # print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()