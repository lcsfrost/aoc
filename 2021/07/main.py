import os
from collections import defaultdict
import math

Y = '2021'
D = '07'


"""
Quick notes and problem description:

WHALE trying to eat me
CRABS trying to save me

Crab submarines are trying to blast a hole for me to escape through
Crabs must be aligned before they have power to blast a hole through

Must make horixzontal positions match while using as little fuel as possible
1 step left/right takes 1 fuel
"""



def solve_part_one():
    l = process_file()
    l.sort()
    midpoint = l[len(l)//2]
    cost = 948235734957349583749583485345834
    for i in range(1000):
        cost = min(cost, calc_linear_fuel_consumption(l, midpoint))
    return cost

def solve_part_two():
    l = process_file()
    midpoint = sum(l)/len(l) #continuous minimum for function
    cost = math.inf
    for i in [math.floor(midpoint), math.ceil(midpoint)]: #need discrete minimum cost for each integer surrounding midpoint
        cost = int(min(cost, calc_exp_fuel_consumption(l, i)))
    return cost

def calc_linear_fuel_consumption(armada, pos):
    fuel_cost = 0
    for crab in armada:
        fuel_cost += abs(pos-crab)
    return fuel_cost

def calc_exp_fuel_consumption(armada, pos):
    total_cost = 0
    for crab in armada:
        dist = abs(crab-pos)
        total_cost += (dist*(dist+1))/2
    return total_cost

def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            for num in line.split(','):
                l.append(int(num.strip()))
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()