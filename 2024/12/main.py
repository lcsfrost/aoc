import sys
import math
import time

start = time.perf_counter()

def process_file():
    d = {}
    with open("input.txt") as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                d[(i,j)] = char
    return d


def define_directions():
    d = [(0,1),
         (0,-1),
         (1,0),
         (-1,0)
         ]
    return d

coords_to_letter_dict = process_file()
# coords_to_letter_dict = process_file_test()

"""
Store regions by their top-left most coordinate (allows for multiple letters to be stored)
Store each coordinate in a nested dict, with matching bordering cells stored?


Number of sides of a plot that do not border on another plot
Create a dict of dict[letters][plots]set(neighbouring_plots)
Can't use letters as a key as there are multiple distinct regions with the same letter but different areas/perimeters.
should be tuple(letter, first_found_spot)? 
For each plot, return len(directions)-neighbouring_plots
"""

def find_region(coords, target_letter, other_regions, region = None, visited_coords = None):
    """Function is intended to be recursively called, with new coords being passed each time."""
    if region is None: #First time calling function
        region = set()

    if visited_coords is None: #First time calling function
        visited_coords = set()

    if coords in visited_coords: #Checking if we have been here before 
        return region, visited_coords #If we've been here before, return region

    visited_coords.add(coords)
    plot_letter = coords_to_letter_dict.get(coords, 0)
    if plot_letter != target_letter: #Not a part of region.
        return region, visited_coords #If we've been here before, return region
    else:
        if coords in other_regions: #
            a = set()
            return set(), set()

        region.add(coords) #Coords are for a matching letter, and has not been visited before.
        for d in define_directions():
            new_coords = (coords[0]+d[0], coords[1]+d[1])
            updated_region, visited_coords = find_region(new_coords, target_letter, other_regions, region, visited_coords)
            region.union(updated_region)
        return region, visited_coords

def find_perimeter(region):
    perimeter = 0
    for coords in region:
        for d in define_directions():
            new_coords = tuple((a+b for a, b in zip(coords,d)))
            if coords_to_letter_dict[coords] != coords_to_letter_dict.get(new_coords,0):
                perimeter += 1 #Letter is the same, perimeter is smaller.
    return perimeter

def find_number_of_sides(region):
    #Need to track:(coords, direction where there is a fence, uhhhhhhh)
    #Need to find the number of unique sides in each region.
    # AAAA
    # BBCD
    # BBCC
    # EEEC
    #In the above example, region "B" would have four sides, each of length 2.
    
    number_of_sides = 0
    visited_coords_and_direction = set()
    for coords in region: #Check each location
        for d in define_directions(): #Check each location in all directions
            t = (coords,d)
            # print(f"Checking tuple {t} against {visited_coords_and_direction}")
            if t in visited_coords_and_direction: #Check if this cell/vector has been included in another fence
                # print(f"{t} is already in {visited_coords_and_direction}")
                continue #Move on to next direction
            new_coords = tuple((a+b for a, b in zip(coords,d))) 
            if coords_to_letter_dict[coords] != coords_to_letter_dict.get(new_coords,0): #Letter is not the same, so this is a fence.
                fence_info = find_length_of_fence(coords, d)
                visited_coords_and_direction |= fence_info
                number_of_sides += 1
    return number_of_sides

def find_length_of_fence(coords, direction):
    visited_cells = set()
    letter = coords_to_letter_dict[coords]
    visited_cells.add((coords, direction))

    def rotate_clockwise(vector):
        x,y = vector
        return (y, -x)

    def rotate_counterclockwise(vector):
        x, y = vector
        return (-y,x)
    #Checking perpendicular direction A

    clockwise_direction = rotate_clockwise(direction)
    new_coords = tuple((a+b for a, b in zip(coords, clockwise_direction)))
    other_side_of_fence_coord = tuple((a+b for a,b in zip(new_coords, direction)))
    while coords_to_letter_dict.get(other_side_of_fence_coord,0) != letter and coords_to_letter_dict.get(new_coords,0) == letter:
        visited_cells.add((new_coords, direction)) #Storing the direction we're currently evaluating.
        new_coords = tuple((a+b for a, b in zip(new_coords, clockwise_direction)))
        other_side_of_fence_coord = tuple((a+b for a, b in zip(new_coords, direction)))


    #Checking perpendicular direction B
    counter_clockwise_direction = rotate_counterclockwise(direction)
    new_coords = tuple((a+b for a, b in zip(coords, counter_clockwise_direction)))
    other_side_of_fence_coord = tuple((a+b for a, b in zip(new_coords, direction)))
    while coords_to_letter_dict.get(other_side_of_fence_coord,0) != letter and coords_to_letter_dict.get(new_coords,0) == letter:
        visited_cells.add((new_coords, direction)) #Storing the direction we're currently evaluating.
        new_coords = tuple((a+b for a, b in zip(new_coords, counter_clockwise_direction)))
        other_side_of_fence_coord = tuple((a+b for a, b in zip(new_coords, direction)))
    return visited_cells



def find_regions():
    unique_regions = {}
    existing_regions = set()
    for coords in coords_to_letter_dict:
        if coords not in existing_regions:
            region_set, visited_coords = find_region(coords, coords_to_letter_dict[coords], existing_regions)
            unique_regions[coords] = region_set
            existing_regions |= region_set
    return unique_regions

def calculate_price(unique_regions, calculation_function):
    price = 0
    for k, v in unique_regions.items():
        area = len(v)
        metric = calculation_function(v)
        price += area * metric
    return price

def part_one(unique_regions):
    total_price = calculate_price(unique_regions, find_perimeter)
    print(f"Total price should be {total_price}")

def part_two(unique_regions):
    total_price = calculate_price(unique_regions, find_number_of_sides)
    print(f"Total price should be {total_price}")

if __name__ == "__main__":
    unique_regions = find_regions()
    part_one(unique_regions)
    part_two(unique_regions)

print(f"{time.perf_counter()-start:.2f}")