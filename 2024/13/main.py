"""
Goal: Win as many prizes as possible with the fewest possible button presses.

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400


Each machine contains one prize; to win the prize you must position the claw ***EXACTLY*** above the prize along both the X and Y axis.

Each button would not need to be pushed more than 100 times to win a prize.

"""
import re

def process_file(filename = "input.txt"):
    button_a_list = []
    button_b_list = []
    prize_coords = []
    with open(filename) as file:
        regex = r"\d+"
        for line in file:
            coords = tuple(map(int, re.findall(regex, line)))
            if 'Button A' in line:
                button_a_list.append(coords)
            elif 'Button B' in line:
                button_b_list.append(coords)
            elif 'Prize' in line:
                prize_coords.append(coords)
    return button_a_list, button_b_list, prize_coords

def solve_part_one(a: list[tuple],b: list[tuple],c: list[tuple]) -> int:
    total_required_tokens = 0
    for a, b, target in zip(a,b,c):
        best_tokens_for_this_machine = 0
        for i in range(101):
            for j in range(101):
                xa, ya = a
                xb, yb = b
                xtarget, ytarget = target
                x_total = xa*i + xb*j
                y_total = ya*i + yb * j
                if x_total == xtarget and y_total == ytarget:
                    required_tokens = (i)*3 + (j)
                    if best_tokens_for_this_machine == 0:
                        best_tokens_for_this_machine = required_tokens
                    else:
                        best_tokens_for_this_machine = min(best_tokens_for_this_machine, required_tokens)
        total_required_tokens += best_tokens_for_this_machine
        print(f"{a}, {b}, {c}, {best_tokens_for_this_machine}")
    return total_required_tokens

def solve_part_two(a: list[tuple],b: list[tuple],c: list[tuple]) -> int:
    total_tokens = 0
    for a, b, target in zip(a,b,c):
        xa, ya = a
        xb, yb = b
        xtarget, ytarget = target
        # xtarget += 10000000000000
        # ytarget += 10000000000000
        i = (yb*xtarget-xb*ytarget)//(yb*xa-xb*ya)
        j = (ya*xtarget-xa*ytarget)//(ya*xb-xa*yb)
        print(i,j)
        if xa*i+xb*j == xtarget and ya*i + yb*j == ytarget:
            token_cost = i*3+j
            total_tokens += token_cost
            print("solved")
    return total_tokens

def main():
    a,b,c = process_file()
    # total_tokens = solve_part_one(a,b,c)
    # print(total_tokens)
    total_tokens = solve_part_two(a,b,c)
    print(total_tokens)

if __name__ == "__main__":
    main()