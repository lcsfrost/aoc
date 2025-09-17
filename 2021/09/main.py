import os

Y = '2021'
D = '09'

"""
Quick notes and problem description:


GOAL:
Find the low points: Locations that are lower than any of its adjacent locations; 
diagonals don't count, edges are ignored.
Ris klevel of a low point is 1 + its height.  Height of 2 = risk of 3

Return sum of risk levels of all low points on heightmap
"""

DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]

def solve_part_one():
    l = process_file()
    row_len = len(l)
    col_len = len(l[0])
    print(row_len, col_len)
    grid = build_dict(l)
    low_point_list = []
    i = 0 
    while i < row_len: #Traverses rows (down)
        j = 0
        while j < col_len: #Traverses columns (right)
            x = grid[(i,j)]
            if _is_low_point(grid, i, j):
                low_point_list.append(x)
            j += 1
        i += 1
    print(low_point_list)
    print(sum(low_point_list))
    print(sum([x +1 for x in low_point_list]))
    return low_point_list

def _is_low_point(grid, i, j):
    val = grid[(i,j)]
    for d in DIRECTIONS:
        new_coord = tuple([a+b for a,b in zip((i,j), d)])
        neighbour_val = grid.get(new_coord, None)
        if neighbour_val is not None:
            print(f"{i= }, {j= }, {val = }, {neighbour_val= }")
            if val >= neighbour_val:
                return False #Cell is higher than at least one neighbour, cell is not a low point.
    return True #Returns true only if all direction checks pass

def traverse_grid(grid, starting_point, visited_locations = None):
    if visited_locations == None:
        visited_locations = set()


def solve_part_two():
    """Find basins
    Basins are the number of neighbouring cells that flow down into the low point.
    Basin walls = edges or 9s?
    1. Loop through low points
    2. Create set of visited points
    3. Traverse all directions until a boundary is met, adding valid points to set
    4. If location in set, stop traversing and return set"""
    l = process_file()
    row_len = len(l)
    col_len = len(l[0])
    print(row_len, col_len)
    grid = build_dict(l)
    low_point_list = []
    i = 0 
    while i < row_len: #Traverses rows (down)
        j = 0
        while j < col_len: #Traverses columns (right)
            x = grid[(i,j)]
            if _is_low_point(grid, i, j):
                low_point_list.append(x)
            j += 1
        i += 1
    print(low_point_list)
    print(sum(low_point_list))
    print(sum([x +1 for x in low_point_list]))
    return low_point_list





def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for i, line in enumerate(file):
            l.append(line.strip())
    return l

def build_dict(l):
    d = {}
    for i, line in enumerate(l):
        for j, char in enumerate(line):
            d[(i,j)] = int(char)
    return d

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {sum([x +1 for x in part_one_ans])}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()