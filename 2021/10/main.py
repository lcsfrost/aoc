import os

Y = '2021'
D = '10'

"""
Quick notes and problem description:

Closure
Ignore incomplete lines
Discard corrupted lines


Corrupted = Expected "]" but found ">" instead
Incomplete = Expected "]" but found end of line? Idk exactly yet.


"""



def solve_part_one():
    l = process_file()
    x = 0
    for line in l:
        x += get_line_score_p1(line)
        
    ans = x
    return ans

def solve_part_two():
    """
    Find incomplete lines, and complete them.
    Incomplete lines will be missing closing brackets only
    
        
    """
    ans = ''
    return ans

BRACKET_DICT = {
    "]":"[",
    "}":"{",
    ")":"(",
    ">":"<",
    "[":"]",
    "{":"}",
    "(":")",
    "<":">",
}

P1_SCORE_DICT = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}

P2_SCORE_DICT = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

def get_line_score_p1(line):
    "Needs to return score of first illegal character (if present) otherwise return 0"
    queue = []
    for char in line:
        if char in ["(", "[", "{", "<"]:
            queue.append(char)
        elif char in [")", "]", "}", ">"]:
            try:
                opening_brace = queue.pop()
                if not BRACKET_DICT[char] == opening_brace:
                    """char is an illegal brace; doesn't match expected closing brace"""
                    return P1_SCORE_DICT[char]
            except IndexError:
                s = "No corresponding opening brace to compare - line is incomplete"
                return 0
    "Line is valid"
    return 0

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