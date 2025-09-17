import os
import time
import math

Y = '2021'
D = '11'

ANSI_COLORS = {
    'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m',
    'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m',
    'cyan': '\033[36m', 'white': '\033[37m', 'reset': '\033[39m'
}

"""
Quick notes and problem description:

Dumbo Octopuses do not like my lights
100 octopuses in a 10 by 10 grid
Octopi gain energy over time and flash brightly when they reach full.

During each step:
1. The energy level of each octopus increases by 1
2. Any octopus with energy GREATER than 9 flashes
 2a. Flashing increases the energy of all adjacent/diagonal octopuses by 1
 2b. If this increases their energy past 9, this also causes a flash.
 2c. NOTE: An octopus can only flash once per step (Use a Set)
3. Any octopus that flashed has its energy set to 0.
"""

class Octopi():
    def __init__(self) -> None:
        self.flash_count = 0
        self.simultaneous_flash_round = math.inf
        self.octopus_grid = self.build_dict()
        self.DIRECTIONS = [(0,1),
                           (0,-1),
                           (1,0),
                           (-1,0),
                           (1,1),
                           (1,-1),
                           (-1,1),
                           (-1,-1)]
        

    def update_octopus(self, coords):
        #Check if octopus has flashed; skip if yes.
        if coords in self.octopus_set:
            return
        octopus_energy = self.octopus_grid[coords] + 1
        if octopus_energy > 9:
            self.flash_octopus(coords) #adds to set, updates nearby octopi.
        else:
            self.octopus_grid[coords] = self.octopus_grid[coords] + 1
    
    def flash_octopus(self, coords):
        if coords in self.octopus_set:
            return
        self.octopus_set.add(coords)
        self.octopus_grid[coords] = 0
        self.flash_count += 1
        for dir_tuple in self.DIRECTIONS:
            new_coords = tuple(map(sum, zip(dir_tuple, coords)))
            if self.octopus_grid.get(new_coords, None) is not None:
                self.update_octopus(new_coords)

    def process_round(self, n = 1, show = False):
        for step in range(n):
            self.octopus_set = set()
            i = 0
            while i < self.grid_size:
                j = 0
                while j < self.grid_size:
                    self.update_octopus((i,j))
                    j += 1
                i += 1
            if len(self.octopus_set) == self.grid_size**2:
                self.simultaneous_flash_round = min(self.simultaneous_flash_round, step+1)
                self.pretty_print_grid()
                return
            if show:
                self.pretty_print_grid()
                time.sleep(0.1)

    def build_dict(self):
        l = process_file()
        self.grid_size = len(l)
        d = {}
        for i, line in enumerate(l):
            for j, char in enumerate(line):
                d[(i,j)] = int(char)
        return d
    
    def pretty_print_grid(self):
        l = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for k, v in self.octopus_grid.items():
            l[k[0]][k[1]] = v
        s = '\n'.join([''.join([str(num) for num in sublist]) for sublist in l])
        # new_l = '\n'.join(''.join([str(x) for x in l]))
        print('\n'*40)
        colour_code = ANSI_COLORS.get('yellow', ANSI_COLORS['reset'])
        s = s.replace("0",f"{colour_code}0{ANSI_COLORS['reset']}")
        print(s)
        print('\n')

def solve_part_one():
    x = Octopi()
    x.process_round(100, show=False)
    x.flash_count
    return x.flash_count

def solve_part_two():
    x = Octopi()
    x.process_round(1000, False)
    return x.simultaneous_flash_round






def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            new_line = []
            for char in line.strip():
                new_line.append(int(char))
            l.append(new_line)
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()