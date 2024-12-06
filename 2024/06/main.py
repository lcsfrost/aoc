
"""RULES
Lab guards:
1. Map shows the current position of the guard with ^ to indicate the guard is currently facing up from the perspective of the map.
2. Obstructions are shown as # on the map
3. Guard movements: If there is something directly in front of you, turn right 90 degrees. 
                    If there is nothing in front, step forwards.
"""

"""
--- Part Two ---
While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...
Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...
Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...
Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...
Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...
Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..
It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?
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
