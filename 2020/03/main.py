from collections import defaultdict
import math

def process_file():
    l = []
    d = defaultdict(str)
    with open("input.txt") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line):
                d[(i,j)] = char #j=x , i=y
            l.append([char for char in line.strip()])
    return l, d


"""In an eternal forest
Starting at the top left corner of the map and following a pattern of right 3 and down 1, how many trees do we encounter?

confirm i,j directions in list thing
first is y, then x 
"""
def part_one():
    forest, forest_dict = process_file()
    tree_count = 0
    toboggan_pos = (0,0)
    dir_vector = (1,3) #Down one row (y) right three columns (x)
    while toboggan_pos[0] < len(forest):
        toboggan_pos = (toboggan_pos[0] + dir_vector[0], (toboggan_pos[1] + dir_vector[1]) % len(forest[0]))
        if forest_dict[toboggan_pos] == "#":
            tree_count += 1
    return tree_count

def part_two():
    forest, forest_dict = process_file()
    tree_count_list = []
    dir_vector_list = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    for dir_vector in dir_vector_list:
        toboggan_pos = (0,0)
        tree_count = 0
        while toboggan_pos[0] < len(forest):
            toboggan_pos = (toboggan_pos[0] + dir_vector[0], (toboggan_pos[1] + dir_vector[1]) % len(forest[0]))
            if forest_dict[toboggan_pos] == "#":
                tree_count += 1
        tree_count_list.append(tree_count)
    return math.prod(tree_count_list)

def main():
    print(part_one())
    print(part_two())
    pass

if __name__ == "__main__":
    main()