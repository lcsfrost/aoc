

#######################################################################

# PART A
# 1. Convert into a matrix (list of lists)
# 2. Use pointers to navigate through matrix

# Ways to match: 
            # 1. Diagonally
            # 2. Horizontally
            # 3. Vertically
            # 4. Backwards in any direction



#######################################################################

class Xmas():
    def __init__(self) -> None:
        self.xmas_list = self.convert_file_to_matrix()
        pass

    def convert_file_to_matrix(self):
        xmas_list = []
        with open('xmas.txt') as f:
            for line in f:
                xmas_list.append(line.strip())
        return xmas_list

    def check_index(self,row_index, col_index):
        index_match_total = 0
        direction_list = [
            (0,0), #GO NOWHERE
            (1,1),   #D
            (-1,-1), #D
            (-1,1),  #D
            (1,-1),  #D
            (0,1), #H
            (0,-1), #H
            (1,0), #V
            (-1,0), #V
        ]
        for row_direction_modifier, col_direction_modifier in direction_list:
            index_match_total += self.check_direction(row_index,col_index,row_direction_modifier,col_direction_modifier)
        return index_match_total

    def check_direction(self, row_index, col_index, row_direction_modifier, col_direction_modifier):
        s = ''
        for i in range(4): #Length of XMAS str
            r = row_index + i * row_direction_modifier
            c = col_index + i * col_direction_modifier
            if r < 0 or c < 0:
                return False
            if r > len(self.xmas_list)-1 or c > len(self.xmas_list[0])-1:
                return False
            s += self.xmas_list[r][c]
        return s == "XMAS"

    def check_for_mas_cross(self, row, col):
        if row < 1 or row > len(self.xmas_list)-2:
            return False
        if col < 1 or col > len(self.xmas_list[0])-2:
            return False
        str_one = self.xmas_list[row-1][col-1] + self.xmas_list[row][col] + self.xmas_list[row+1][col+1]
        str_two = self.xmas_list[row+1][col-1] + self.xmas_list[row][col] + self.xmas_list[row-1][col+1]
        str_one_check = str_one == 'MAS' or str_one[::-1] == 'MAS'
        str_two_check = str_two == 'MAS' or str_two[::-1] == 'MAS'
        return str_one_check and str_two_check

def solve_part_one():
    x = Xmas()
    # print(x.xmas_list)
    total_matches = 0
    try:
        for i in range(0,140):
            for j in range(0,140):
                total_matches += x.check_index(i,j)
    except Exception as e:
        print(e)
        print(i,j)
    return total_matches

def solve_part_two():
    x = Xmas()
    total_matches = 0
    for i in range(0,140):
        for j in range(0,140):
            total_matches += x.check_for_mas_cross(i,j)
    return total_matches

if __name__ == "__main__":
    part_one_matches = solve_part_one()
    part_two_matches = solve_part_two()
    print(f"{part_one_matches = }")
    print(f"{part_two_matches = }")