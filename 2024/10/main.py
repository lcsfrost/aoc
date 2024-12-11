import sys
import time
import os

def process_file():
    d = {}
    with open('input.txt') as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.strip()):
                d[(i,j)] = char
    return d

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

location_dict = process_file()
trailheads = []

for xy in location_dict:
    if location_dict[xy] == '0': #starting point found
        trailheads.append(xy)

def find_trails(coords, trail=None):
    if trail is None:
        trail = [coords]
    else:
        trail = trail + [coords] 

    if location_dict[coords] == '9':  # Success condition
        build_grid(trail)
        return [trail]  # Return the entire path to this location
    else:
        valid_paths = []
        for d in directions:  # Loop through possible directions
            new_xy = (coords[0] + d[0], coords[1] + d[1])  # Calculate new coordinates
            build_grid(trail+[new_xy])
            if int(location_dict.get(new_xy, 0)) - int(location_dict[coords]) == 1:  # Check if the new cell is 1 greater
                valid_paths += find_trails(new_xy, trail)  # Recursively find trails from the new coordinate
        return valid_paths  # Return the list of valid paths

def solve_part_one():
    #need to return total number of unique endpoints PER TRAILHEAD
    valid_paths = []
    counter = 0
    for trail in trailheads:
        s = set()
        p = [trail]
        trailhead_summit_paths = find_trails(coords=trail, trail=p)
        valid_paths += trailhead_summit_paths
        for path in trailhead_summit_paths:
            s.add(path[-1])
        counter += len(s)
    return counter

def solve_part_two():
    #need to return all possible paths
    valid_paths = []
    for trail in trailheads:
        valid_paths += find_trails(trail)
    return valid_paths



def build_grid(trail):
    # print("\n"*30)
    l = []
    start_x, start_y = trail[0]
    for i in range(-9,10):
        row = []
        for j in range(-9,10):
            try:
                new_coords = (start_x+i, start_y+j)
                new_val = (location_dict[new_coords])
                # if new_coords == trail[-1] and location_dict.get(new_coords, 0) == 9:
                if new_coords == trail[-1] and location_dict[new_coords] == '9':
                    row.append(f"{bcolors.OKGREEN}{new_val}{bcolors.ENDC}")
                elif new_coords == (start_x, start_y):
                    row.append(f"{bcolors.OKCYAN}{new_val}{bcolors.ENDC}")
                elif new_coords in trail:
                    row.append(f"{bcolors.WARNING}{new_val}{bcolors.ENDC}")
                else:                    
                    row.append(new_val)
            except Exception as e:
                row.append(bcolors.OKBLUE+"#"+bcolors.ENDC)
        l.append(' '.join(row))
    os.system('cls')
    print('\n'.join(l), end="\r")
    
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.HEADER + " hey" + bcolors.ENDC)
print(bcolors.OKBLUE + " hey" + bcolors.ENDC) # Origin?
print(bcolors.OKCYAN + " hey" + bcolors.ENDC)
print(bcolors.OKGREEN + " hey" + bcolors.ENDC) #Successful path
print(bcolors.WARNING + " hey" + bcolors.ENDC) #Brown - good colour for path
print(bcolors.FAIL + " hey" + bcolors.ENDC) #Red - Good colour for bad path


if __name__ == "__main__":
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(part_two_ans[0])
    print(location_dict[part_two_ans[0][0]])
    print(f"{bcolors.HEADER} {part_one_ans = }   {len(part_two_ans) = }{bcolors.ENDC}" + bcolors.OKGREEN + " hey" + bcolors.ENDC + bcolors.HEADER + " hey" + bcolors.ENDC)