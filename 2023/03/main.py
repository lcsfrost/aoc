import re
""" NOT SOLVED IDK MAN I HATE POINTERS"""

class PartSolver():
    def __init__(self) -> None:
        self.part_list = self.load_file()

    def process_part_list(self):
        row = 0
        col = 0
        row_boundary = len(self.part_list)
        col_boundary = len(self.part_list[0])
        while row < row_boundary:
            print(self.part_list[row])
            while col < col_boundary:
                char = self.part_list[row][col]
                s = ''
                if char.isnumeric():
                    temp_num = col
                    while char.isnumeric():
                        s += char
                        temp_num += 1
                        char = self.part_list[row][temp_num]
                        print(s)
                    print(char)
                col +=1
            col = 0
            row += 1

    def load_file(self):
        l = []
        with open('parts.txt') as f:
            for line in f:
                cs = []
                for char in line.strip():
                    cs.append(char)
                l.append(cs)
            return l
        
    def check_row_for_nums(self, row_num):
        pass

    def check_for_adjacent_characters(self):
        pass


def main():
    x = PartSolver()
    x.process_part_list()


if __name__ == "__main__":
    main()