import sys

"""Part 1 goals:
1. Solve maze
2. Find lowest SCORE to endpoint

Moving one step forward = 1 point
Turning by 90 degrees = 1000 points. NOTE: clockwise and counterclockwise spins both == 1000 pts.
Reindeer starts facing EAST.

valid

In dict store the current score required to reach that location? Only update if a shorter path is found 

Solution will be: Pull score where maze coords in dict, regardless of direction?
"""
sys.setrecursionlimit(10000)


def relative_dir_list(direction):
    def rotate_clockwise(xy):
        x, y = xy
        return y, -x

    def rotate_counterclockwise(xy):
        x, y = xy
        return -y, x

    return [
        (1, direction),
        (1000, rotate_clockwise(direction)),
        (1000, rotate_counterclockwise(direction)),
        (2000, rotate_counterclockwise(rotate_counterclockwise(direction))),
    ]

def next_step(coords, dir):
    x1, y1 = coords
    x2, y2 = dir
    return x1 + x2, y1 + y2

def build_maze_from_source():
    l = {}
    with open('input.txt') as file:
        for i, line in enumerate(file):
            for j, char in enumerate(line.strip()):
                l[(i, j)] = char
    return l

def find_maze_path(maze, score, coords, direction=None, visited_dict=None):
    if visited_dict is None:
        visited_dict = {}
    if direction is None:
        direction = (0, 1)

    key = (coords, direction)
    if visited_dict.get(key, float('inf')) <= score:
        return None

    visited_dict[key] = score
    if maze.get(coords, 0) == "E":
        return score

    best_score = float('inf')
    for score_mod, new_direction in relative_dir_list(direction):
        next_cell = next_step(coords, new_direction)

        if maze.get(next_cell, 0) == "#":
            continue

        result = find_maze_path(maze, score + score_mod, next_cell, new_direction, visited_dict)

        if result is not None:
            best_score = min(best_score, result)

    return best_score if best_score != float('inf') else None

def find_reindeer_start(d):
    for k, v in d.items():
        if v == 'S':
            return k

def main():
    maze = build_maze_from_source()
    reindeer_starting_coord = find_reindeer_start(maze)
    result = find_maze_path(maze, 0, reindeer_starting_coord)
    print(f"Lowest score: {result}")

if __name__ == "__main__":
    main()
