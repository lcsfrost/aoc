import os
from functools import cache
import math

Y = '2021'
D = '06'

"""
Quick notes and problem description:

LANTERNFISH
Growth rate modelling
New lanternfish once every 7 days
Lanternfish can be modelled as number of days until it creates a new lanternfish

timer of 3:
after one day: 2
after 2 days: 1
after 3 days: 0
after 4 days: resets to 6, and creates a new lanternfish with internal timer of 8

Per day:
iterate through list of currently spawned lanternfish
Update their timers in place
Append 
"""

# @cache
# def calc_fish(fish_set, day = 0, target = 80):
#     if day == target:
#         return len(fish_set)
#     end = len(fish_set)
#     i = 0
#     new_fishes = []
#     for i in fish_set:
#         if i == 0:
#             new_fishes.append(6) # Resetting counter to 6
#             new_fishes.append(8) # New fish added with base timer of 8
#         else:
#             new_fishes.append(i-1)
#     return calc_fish(tuple(new_fishes), day + 1, target)
fish_dict = {}


def solve_part_one():
    fish_dict = {}
    l = process_file()
    target = 80
    total = 0
    for i, fish in enumerate(l):
        total += calc_fish(fish, 0, target)
        print(f"finished fish {i}")
    return total

def calc_fish(fish, day, target):
    if day == target:
        return 1 
    
    if (day, fish, target) in fish_dict:
        return fish_dict[(day, fish, target)]
    
    new_fish = []
    if fish == 0:
        new_fish.append(6)
        new_fish.append(8)
    else:
        new_fish.append(fish-1)
    total_count = sum(calc_fish(s, day + 1, target) for s in new_fish)

    fish_dict[(day, fish, target)] = total_count
    return total_count

def solve_part_two():
    l = process_file()
    target = 256
    total = 0
    for i, fish in enumerate(l):
        total += calc_fish(fish, 0,target)
        print(f"finished fish {i}")
    return total

def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            for char in line.split(','):
                l.append(int(char))
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()