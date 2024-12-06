import re


def load_file():
    l = []
    with open('input.txt') as f:
        for line in f:
            l.append(line)
        return l
    
def extract_numbers(line):
    regex = r"\d{1,100}"
    card_num, line_without_game_number = line.split(":")
    card_num = int(re.findall(regex, card_num)[0])
    winning_nums, picked_nums = line_without_game_number.split("|")
    winning_nums = [int(x) for x in re.findall(regex, winning_nums)]
    picked_nums = [int(x) for x in re.findall(regex, picked_nums)]
    return winning_nums, picked_nums

def get_card_count():
    pass


def get_line_score(winning_nums, picked_nums):
    card_value = 0
    matched_nums = []
    for i in picked_nums:
        if i in winning_nums:
            matched_nums.append(i)
            if card_value == 0:
                card_value += 1
            else:
                card_value *= 2
    print(f"""
{winning_nums} | {picked_nums}
{matched_nums = }
{card_value = }


""")
    return card_value

def main():
    total = 0
    for i in load_file():
        winning_nums, picked_nums = extract_numbers(i)
        total += get_line_score(winning_nums, picked_nums)
    print(total)

main()
"List of winning numbers | list of numbers you have."

