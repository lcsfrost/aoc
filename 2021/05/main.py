import os

Y = '2021'
D = '05'
GRID_SIZE = 1000
"""
Quick notes and problem description:





"""



def solve_part_one():
    l = process_file()
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for coord_pair in l:
        x1 = coord_pair[0][0]
        y1 = coord_pair[0][1]
        x2 = coord_pair[1][0]
        y2 = coord_pair[1][1]
        if x1 == x2:
            x = x1
            start = min(y1, y2)
            end = max(y1,y2) + 1
            for y in range(start, end):
                grid[y][x] = grid[y][x] +1
        if y1 == y2:
            y = y1
            start = min(x1, x2)
            end = max(x1,x2) + 1
            for x in range(start, end):
                grid[y][x] = grid[y][x] +1
    score_grid(grid)

def score_grid(grid):
    score = 0
    for i in grid:
        for j in i:
            if j > 1:
                score += 1
    print(score)

# def solve_part_two():
#     l = process_file()
#     grid = [[0 for _ in range(10)] for _ in range(10)]
#     for coord_pair in l:
#         x1 = coord_pair[0][0]
#         y1 = coord_pair[0][1]
#         x2 = coord_pair[1][0]
#         y2 = coord_pair[1][1]
#         print([x1, y1], [x2, y2])
#         start_x = min(x1,x2)
#         end_x = max(x1,x2) + 1
#         start_y = min(y1, y2)
#         end_y = max(y1, y2) + 1
#         if x1 == x2:
#             x = x1
#             for y in range(start_y, end_y):
#                 grid[x][y] = grid[x][y] +1
#         elif y1 == y2:
#             y = y1
#             for x in range(start_x, end_x):
#                 grid[x][y] = grid[x][y] +1
#         elif abs(y1-y2) == abs(x1-x2): #Lines are diagonal
#             for x, y in zip(range(start_x, end_x), range(start_y, end_y)):
#                 grid[x][y] = grid[x][y] +1
#     score_grid(grid)
#     show_grid(grid)

def solve_part_two():
    import time
    l = process_file()
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for coord_pair in l:
        x1 = coord_pair[0][0]
        y1 = coord_pair[0][1]
        x2 = coord_pair[1][0]
        y2 = coord_pair[1][1]
        start_x = min(x1,x2)
        end_x = max(x1,x2) + 1
        start_y = min(y1, y2)
        end_y = max(y1, y2) + 1
        line_type = ''
        if x1 == x2:
            x = x1
            line_type = 'vertical'
            for y in range(start_y, end_y):
                grid[y][x] = grid[y][x] +1
        elif y1 == y2:
            y = y1
            line_type = 'horizontal'
            for x in range(start_x, end_x):
                grid[y][x] = grid[y][x] +1
        elif abs(y1-y2) == abs(x1-x2): #Lines are diagonal
            line_type = 'diagonal'
            x_direction = get_direction(x1, x2)
            y_direction = get_direction(y1, y2)
            # print(x1, x2, x_direction, y1, y2, y_direction)
            for x, y in zip(range(x1, x2+x_direction, x_direction), range(y1, y2+y_direction, y_direction)):
                grid[y][x] = grid[y][x] +1
        # print(line_type, [x1, y1], [x2, y2])
        # show_grid(grid)
        # time.sleep(1)
    return score_grid(grid)

def get_direction(n1, n2):
    if n1 < n2:
        return 1
    elif n2 < n1:
        return -1
    else:
        return 0


def show_grid(grid):
    for i in grid:
        print(i)



def process_file():
    l = []
    if os.path.basename(os.getcwd()) == 'aoc':
        input_path = os.path.join(os.getcwd(), Y,D,"input.txt")
    else:
        input_path = "input.txt"
    with open(input_path) as file:
        for line in file:
            a, b = line.strip().split(' -> ')
            a = [int(x) for x in a.split(',')]
            b = [int(x) for x in b.split(',')]
            l.append([a,b])
            # l.append(line.strip().split(' -> '))
    return l

def main():
    part_one_ans = solve_part_one()
    part_two_ans = solve_part_two()

    print(f"Part one answer: {part_one_ans}")
    print(f"Part two answer: {part_two_ans}")

if __name__ == "__main__":
    main()