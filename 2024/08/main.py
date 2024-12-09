from collections import defaultdict


class ProbemSolver():
    def __init__(self):
        self.char_dict = defaultdict(list)
        self.antinode_dict = defaultdict(set)
        self.resonant_antinode_dict = defaultdict(set)
        self.file = self.process_file()
        self.i_boundary = len(self.file)-1
        self.j_boundary = len(self.file[0])-1
        self.get_character_locations()
        self.calculate_antinodes()
        self.recalc_with_resonant_harmonics()
        self.part_1_answer()
        self.part_2_answer()

    def part_1_answer(self):
        new_set = set()
        for k, v in self.antinode_dict.items():
            new_set.update(v)
        print(len(new_set))
    
    def part_2_answer(self):
        new_set = set()
        for k, v in self.resonant_antinode_dict.items():
            new_set.update(v)
        print(len(new_set))

    def get_character_locations(self):
        for row_index, row in enumerate(self.file):
            for column_index, char in enumerate(row):
                if char != '.':
                    self.char_dict[char].append((row_index,column_index))
        pass

    def calculate_antinodes(self):
        for character, node_list in self.char_dict.items():
            if len(node_list) < 2:
                continue #If there is only one node, no antinodes exist.
            for node_1 in node_list:
                for node_2 in node_list:
                    i_1, j_1 = node_1 #Coordinates of first node
                    i_2, j_2 = node_2
                    if i_1 == i_2 and j_1 == j_2:
                        continue #Same node - don't need to evaluate
                    i_difference = i_1-i_2
                    j_difference = j_1-j_2

                    new_node_1 = (i_1+i_difference, j_1+j_difference)
                    new_node_2 = (i_2-i_difference, j_2-j_difference)

                    if self.bounds_check(new_node_1):
                        self.antinode_dict[character].add(new_node_1)
                    if self.bounds_check(new_node_2):
                        self.antinode_dict[character].add(new_node_2)
                        
    def recalc_with_resonant_harmonics(self):
        for character, node_list in self.char_dict.items():
            for node_1 in node_list:
                for node_2 in node_list:
                    if node_1 == node_2:
                        continue #Same node - don't need to evaluate.
                    i_1, j_1 = node_1 #Coordinates of first node
                    i_2, j_2 = node_2
                    difference_vector = (i_1-i_2, j_1-j_2)
                    loop_count = 0
                    while self.bounds_check(coords= node_1, loop_count=loop_count, vector= difference_vector):

                        self.resonant_antinode_dict[character].add(self.new_vector)
                        loop_count += 1
                    loop_count = 0
                    while self.bounds_check(coords= node_2, loop_count=loop_count, vector= difference_vector):
                        self.resonant_antinode_dict[character].add(self.new_vector)
                        loop_count -= 1
                
    def bounds_check(self, coords, loop_count = 0, vector = (0,0)):
        i_diff, j_diff = vector
        i_diff *= loop_count
        j_diff *= loop_count
        i = coords[0] + i_diff
        j = coords[1] + j_diff
        self.new_vector = (i,j)
        if i < 0 or i > self.i_boundary:
            return False
        if j < 0 or j > self.j_boundary:
            return False
        return True

    def process_file(self):
        l = []
        with open("input.txt") as file:
            for line in file:
                l.append(line.strip())
        return l

def main():
    ProbemSolver()


if __name__ == "__main__":
    main()