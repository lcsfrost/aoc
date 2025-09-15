import os
import numpy as np

Y = '2021'
D = '02'
DIRDICT = {'up': np.array([0,1]),
           'down': np.array([0,-1]),
           'forward':np.array([1,0]),
           'backward':np.array([-1,0])
           }

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

def parse_instructions(s:str):
    x = s.split(' ')
    instruction, scalar = x[0], x[-1]

    return instruction, int(scalar)

def update_position(pos,direction,scalar):
    return pos + direction * scalar

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

def solve_part_one():
    l = (process_file())
    pos = np.array([0,0])

    for line in l:
        old_pos = pos
        instruction, scalar = parse_instructions(line)
        direction = DIRDICT[instruction]
        pos = update_position(pos, direction, scalar)
    print(pos)
    ans = ''
    return ans

def solve_part_two():
    l = (process_file())
    pos = np.array([0,0])
    aim = 0
    for line in l:
        old_pos = pos
        instruction, scalar = parse_instructions(line)
        direction = DIRDICT[instruction]
        if instruction == "up":
            aim -= scalar
        elif instruction == "down":
            aim += scalar
        elif instruction == 'forward':
            direction = np.array([scalar,aim*scalar])
            pos = update_position(pos, direction, 1)
        print(f"{instruction: <10} {str(direction): <10} {str(old_pos): <10} {str(pos): <10}")
    print(pos)
    ans = ''
    return ans

if __name__ == "__main__":
    main()