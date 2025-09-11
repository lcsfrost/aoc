from collections import defaultdict
from operator import *
import math

def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            l.append(line.strip())
    return l

def main():
    l = process_file()
    num_rows = len(l)
    num_cols = len(l[0])
    max_col_index = num_cols - 1
    max_row_index = num_rows - 1
    d = {}
    def _is_tree_visible(row_index, col_index) -> bool:
        height = l[row_index][col_index]
        if row_index == 0 or row_index == max_row_index:
            return True #Tree is on edge of grid
        if col_index == 0 or col_index == max_col_index:
            return True #Tree is on edge of grid
        
        #Traverse left (index decreases)
        tree_list = []
        i = row_index-1
        while i >=0: 
            tree_list.append(l[i][col_index])
            i -= 1
        if not any([x>=height for x in tree_list]):#No trees greater than height
            return True
        
        # Traverse Right (index increases)
        tree_list = []
        i = row_index + 1
        while i <= max_row_index: 
            tree_list.append(l[i][col_index])
            i += 1
        if not any([x>=height for x in tree_list]):#No trees greater than height
            return True
        
        #Traverse Up (index decreases)
        tree_list = []
        j = col_index - 1
        while j >= 0: 
            tree_list.append(l[row_index][j])
            j -= 1
        if not any([x>=height for x in tree_list]):#No trees greater than height
            return True

        tree_list = []
        j = col_index + 1
        while j <= max_col_index: #Traverse Down (index increases)
            tree_list.append(l[row_index][j])
            j += 1
        if not any([x>=height for x in tree_list]):#No trees greater than height
            return True
        return False
    for i in range(num_rows):
        for j in range(num_cols):
            d[(i,j)] = _is_tree_visible(i,j)
    print(f"Visible trees: {countOf(d.values(), True)}")
    print(f"Invisible trees: {countOf(d.values(), False)}")


def main_part_two():
    l = process_file()
    num_rows = len(l)
    num_cols = len(l[0])
    max_col_index = num_cols - 1
    max_row_index = num_rows - 1
    max_tree_score = 0
    d = {}
    def _calc_tree_score(row_index, col_index) -> bool:
        if row_index == 0 or row_index == max_row_index:
            return 0 #Tree is on edge of grid
        if col_index == 0 or col_index == max_col_index:
            return 0 #Tree is on edge of grid; view_score is 0
        height = l[row_index][col_index]

        dist_list = []

        #Traverse up (row index decreases)
        found_tree = False
        i = row_index -1
        while i >=0:
            if l[i][col_index] >= height:
                dist_list.append(abs(row_index-i))
                found_tree = True
                break
            i -= 1
        if found_tree == False:
            dist_list.append(row_index)
        
        #Traverse down (row index increases)
        found_tree = False
        i = row_index +1
        while i <= max_row_index:
            if l[i][col_index] >= height:
                dist_list.append(abs(row_index-i))
                found_tree = True
                break
            i += 1
        if found_tree == False:
            dist_list.append(abs(max_row_index-row_index))
        
        #Traverse left (col index decreases)
        found_tree = False
        j = col_index -1
        while j >= 0:
            if l[row_index][j] >= height:
                dist_list.append(abs(col_index-j))
                found_tree = True
                break
            j -= 1
        if found_tree == False:
            dist_list.append(abs(col_index))

        #Traverses right (col index increases)
        found_tree = False
        j = col_index +1
        while j <= max_col_index:
            if l[row_index][j] >= height:
                dist_list.append(abs(col_index-j))
                found_tree = True
                break
            j += 1
        if found_tree == False:
            dist_list.append(abs(max_col_index-col_index))
        return math.prod(dist_list)

    for i in range(num_rows):
        for j in range(num_cols):
            max_tree_score = max(max_tree_score, _calc_tree_score(i,j))
    print(max_tree_score)

if __name__ == "__main__":
    main()
    main_part_two()





"""
Input is a map of all tree heights
Tree is represented by a single digit whose value is its height
A tree is visible if all other trees between it and each 
grid edge is shorter than it


All trees on a grid edge are automatically visible


How many trees are visible from outside the grid?

if row or column == 0 or max len, isvisible.
"""