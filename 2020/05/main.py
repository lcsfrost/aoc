import re
"""
Lost boarding pass
Airline uses binary space partitioning to seat people
A seat might be specified like:
A seat might be specified like FBFBBFFRLR, where F means "front",
    B means "back", L means "left", and R means "right".

Binary search:
range(128)
range(8)    


"""

PASS_DICT = {#Subtracting powers of 2 to get index of seat.
    "F":1,
    "B":0,
    "L":1,
    "R":0,
} 
"""
index = 128
for i, char in enumerate(l[0],-len(l[0])):
    index += PASS_DICT[char]
"""

def process_file()->list[str,str]:
    l = []
    with open("input.txt") as file:
        for line in file:
            
            l.append(re.findall(r"[FB]+|[RL]+", line))
    return l

    

# def f(l):
# ...     bits = len(l)
# ...     seats = 2**bits
# ...     print(seats)
# ...     for i, bit in enumerate(l,-bits):
# ...         if bit:
# ...             print(bit)
# ...         print(2**abs(i), abs(bit))


def find_seat_coords(boarding_pass, row_bits, col_bits):
    row = 2**row_bits -1 #convert to 0-based
    col = 2**col_bits -1 #convert to 0-based 
    for i, char in enumerate(boarding_pass[0], -row_bits):#Rows
        if PASS_DICT[char]:
            row -= PASS_DICT[char] * (2**abs(i)>>1)
        print(f"{2**abs(i)>>1: >3} | {char} | {row: >3} | {col: >3} | {PASS_DICT[char]}")
    for i, char in enumerate(boarding_pass[1], -col_bits):
        if PASS_DICT[char]:
            col -= PASS_DICT[char] * (2**abs(i)>>1)
        print(f"{2**abs(i)>>1: >3} | {char} | {row: >3} | {col: >3} | {PASS_DICT[char]}")
        
    print((row, col), "\n\n")
    return (row,col)

def build_plane_matrix(row_bits, col_bits):
    cols = 2**col_bits
    rows = 2**row_bits
    # print(rows, cols)
    return [[(i,j) for j in range(cols)] for i in range(rows)]

def score_seat(coords):
    print(coords)
    return coords[0]*8+coords[1]

test_passes = [["BFFFBBF","RRR"], ["FFFBBBF","RRR"], 
               ["BBFFBBF","RLL"], ["FBFBBFF","RLR"]]
def main():
    boarding_passes_list = process_file()
    row_bits = len(boarding_passes_list[0][0])
    col_bits = len(boarding_passes_list[0][1])
    seats_matrix = build_plane_matrix(row_bits, col_bits)
    max_score = 0
    for i in boarding_passes_list:
        coords = find_seat_coords(i, row_bits, col_bits)
        seats_matrix[coords[0]][coords[1]] = 1
        max_score = max(max_score, score_seat(coords))
        print(max_score)
    draw_plane(seats_matrix)

def draw_plane(seats_matrix):
    for row in seats_matrix:
        print(row)
if __name__ == "__main__":
    main()