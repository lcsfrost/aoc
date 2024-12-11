
"""RULES
Lab guards:
1. Map shows the current position of the guard with ^ to indicate the guard is currently facing up from the perspective of the map.
2. Obstructions are shown as # on the map
3. Guard movements: If there is something directly in front of you, turn right 90 degrees. 
                    If there is nothing in front, step forwards.
"""

import sys
import copy

class PuzzleSolver():
    def __init__(self):
        sys.setrecursionlimit(10000)
        self.guard_state = "^" #checked and overwritten when processing file
        self.guard_position = (0,0) #Checked and overwritten when processing file
        self.maze = self.process_file()
        self.build_dicts()
        self.distinct_positions = set()
        self.blocking_barriers = set()
        self.barrier_list = []
        self.solve_maze()
        c = 0
        loops_detected = 0
        for i, j in self.distinct_positions:
            original_char = self.maze[i][j]
            self.maze[i][j] = "#"
            c += 1
            print(c)
            try:
                self.guard_position = self.og_guard_position
                self.guard_state = self.og_guard_state
                print(self.guard_position, self.guard_state)
                self.solve_maze(track_moves= False, new_barrier_pos=(i,j))
            except RecursionError:
                loops_detected += 1
                pass
            except Exception as error:
                print(f"{error = } | {(i,j) = }")
            finally:
                self.maze[i][j] = original_char
        print(loops_detected)

    def solve_maze(self, track_moves = True, new_barrier_pos = None):
        if new_barrier_pos != None:
            i, j = new_barrier_pos
            self.maze[i][j] = "#"
        i_mod, j_mod = self.vector_dict[self.guard_state]
        i_pos, j_pos = self.guard_position
        i_new = i_pos + 1 * i_mod
        j_new = j_pos + 1 * j_mod
        if i_new < 0 or j_new < 0:
            return True
        if i_new > len(self.maze)-1 or j_new > len(self.maze[0])-1:
            return True
        next_cell = self.maze[i_new][j_new]
        # print(F"{self.guard_position = }, {self.guard_state = }, {next_cell}")
        if next_cell == "#":
            self.guard_state = self.next_orientation_dict[self.guard_state]
        else:
            if track_moves == True:
                self.distinct_positions.add(self.guard_position)
            self.guard_position = (i_new, j_new)
        self.solve_maze(track_moves, new_barrier_pos)

    def build_dicts(self):
        self.vector_dict = {
            "^": (-1,0),
            ">": (0,1),
            "<": (0,-1),
            "V": (1,0),
        }
        self.next_orientation_dict = {
            "^": ">",
            ">": "V",
            "V": "<",
            "<": "^",
        }

    def process_file(self):
        l = []
        guard_position = ''
        with open('maze.txt') as file:
            for i, line in enumerate(file):
                char_list = []
                for j, char in enumerate(line.strip()):
                    char_list.append(char)
                    if char in ["<",">","V","^"]:
                        self.guard_state = char
                        self.guard_position = (i,j)
                        self.og_guard_state = char
                        self.og_guard_position = (i,j)
                l.append(char_list)
        return l


if __name__ == "__main__":
    x = PuzzleSolver()
    print(len(x.distinct_positions))
