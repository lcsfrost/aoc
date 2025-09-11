import re
from collections import defaultdict
import time





def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.replace('\n',''))
    return l

def parse_stack(l:list) -> dict[int: list[str]]:
    stack_rows = l[8::-1]
    stacks_dict = defaultdict(list)
    for i in stack_rows:
        for j in range(9):
            col_num = j+1
            col_pos = j*4+1
            if i[col_pos] != ' ' and i[col_pos].isalpha():
                stacks_dict[col_num].append(i[col_pos])
    # print(stacks_dict)

    return stacks_dict

def parse_instructions(l) -> list[tuple]:
    instructions = []
    """QtyToMove | Start | End"""
    for row in l[10::]:
        instruction_set = re.findall(r"\d+", row)
        instruction_set = tuple(map(int, instruction_set))
        instructions.append(instruction_set)
    return instructions

def move_boxes_part_one(stack_dict:dict, instruction:tuple) -> dict:
    qty = instruction[0]
    from_col = instruction[1]
    to_col = instruction[2]
    for i in range(qty):
        x = stack_dict[from_col].pop()
        stack_dict[to_col].append(x)
        s = ''
        for k,v in stack_dict.items():
            s += f"{k} {v}\n"
            # print(k, v)

        print("\n"*50+s)
        # time.sleep(0.1)
        # print(stack_dict)
    return stack_dict

def move_boxes_part_two(stack_dict:dict, instruction:tuple) -> dict:
    qty = instruction[0]
    from_col = instruction[1]
    to_col = instruction[2]
    in_transit_stack = []
    for i in range(qty):
        in_transit_stack.append(stack_dict[from_col].pop())
    for crate in in_transit_stack[::-1]:
        stack_dict[to_col].append(crate)
    s = ''
    for k,v in stack_dict.items():
        s += f"{k} {v}\n"
    print("\n"*50+s)
    return stack_dict

def main():
    l = process_file()
    stack_dict = parse_stack(l)
    print(stack_dict)
    instructions = parse_instructions(l)
    for i in instructions:
        stack_dict = move_boxes_part_two(stack_dict=stack_dict, instruction=i)
    pass


if __name__ == "__main__":
    main()