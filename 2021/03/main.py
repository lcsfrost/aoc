import os
from Config import config
from collections import defaultdict


Y = '2021'
D = '03'

"""
Quick notes and problem description:

Diagnostic report - power consumption.
Each row has gamma rate and epsilon rate.
Power consumption = gamma * epsilon

Gamma = most common bit in the corresponding position of all numbers in input

With:
110
101
101

Gamma = 101

Epsilon is opposite; least common.


PART TWO:
Life support rating:
Multiply Oxygen generator rating by CO2 Scrubber rating



"""



def solve_part_one():
    l = process_file()
    d = defaultdict(int)
    mid = len(l)/2
    for line in l:
        for i, char in enumerate(line):
            d[i] += int(char)
    gamma = [1 if v > mid else 0 for x, v in d.items()]
    eps = [1 if v < mid else 0 for x, v in d.items()]
    gamma = ''.join([str(x) for x in gamma])
    eps = ''.join([str(x) for x in eps])
    print(d)
    return int(gamma,2) * int(eps,2)

def solve_part_two():
    l = process_file()
    oxy = get_oxygen_rating(l)
    l = process_file()
    scrubber = get_scrubber_rating(l)
    print(oxy, scrubber)
    oxy = int(oxy[0],2)
    scrubber = int(scrubber[0],2)
    print(oxy*scrubber)
    return oxy*scrubber

def get_oxygen_rating(l):
    j = 0
    while j < len(l[0]):
        mid_floor = len(l) /2
        bit_sum = sum([int(x[j]) for x in l])
        most_common_bit = 1 if bit_sum >= mid_floor else 0
        i = 0
        while i < len(l):
            if len(l) == 1:
                return l
            if l[i][j] == str(most_common_bit):
                i += 1
            else:
                l.pop(i)
        j += 1
    return l

def get_scrubber_rating(l):
    j = 0
    while j < len(l[0]):
        mid_floor = len(l) /2 #finds midpoint of list
        bit_sum = sum([int(x[j]) for x in l]) #Counts all the '1's in that position.
        # bit_sum = 500
        least_common_bit = 0 if bit_sum >= mid_floor else 1
        i = 0
        print(f"{j=}, {mid_floor=}, {bit_sum=}, {least_common_bit=}")
        print(l)
        while i < len(l):
            if len(l) == 1:
                return l
            if l[i][j] == str(least_common_bit):
                i += 1
            else:
                l.pop(i)
        j += 1
    return l

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