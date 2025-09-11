INSTRUCTION_VECTOR = {
'R':(0,1),
'L':(0,-1),
'D':(1,0),
'U':(-1,0)
}




def process_file():
    l = []
    with open("input.txt") as file:
        for line in file:
            direction, magnitude = line.strip().split(' ')
            l.append([direction, int(magnitude)])
    return l



def main():
    x = SnakeyBoy()
    x.execute_part_one_instructions()
    pass

class SnakeyBoy():
    def __init__(self) -> None:
        self.rope = [[0,0] for _ in range(10)]
        self.head_pos = [0,0]
        self.tail_pos = [0,0]
        self.instructions = process_file()
        self.tail_position_history = set()
        self.tail_position_history.add(tuple(self.tail_pos))
        self.rope_pos_history = set()
        self.rope_pos_history.add(tuple(self.tail_pos))

    def _tail_needs_update(self):
        #shows difference: [-3, 5]
        position_delta = [a-b for a,b in zip(self.head_pos, self.tail_pos)]
        if any([abs(x) > 1 for x in position_delta]): #Not touching head
            self.update_tail(position_delta)
            self.tail_position_history.add(tuple(self.tail_pos))
            self.update_rope()
            self.rope_pos_history.add(tuple(self.rope[-1]))
            return True
        return False

    def update_rope(self):
        #shows difference: [-3, 5]
        i = 1
        while i <= len(self.rope)-1:
            print(self.rope)
            position_delta = [a-b for a,b in zip(self.rope[i-1], self.rope[i])]
            if any([abs(x) > 1 for x in position_delta]): #Not touching head
                direction = self.normalize_vector_to_direction(position_delta)
                self.rope[i] = [a + b for a, b in zip(direction, self.rope[i])]
            i += 1

    def update_head(self, instruction):
        direction = INSTRUCTION_VECTOR[instruction[0]]
        magnitude = instruction[1]
        change_vector = [x*magnitude for x in direction]
        self.head_pos = [a+b for a,b in zip(self.head_pos, change_vector)]
        self.rope[0] = self.head_pos
        return

    def update_tail(self, pos_delta):
        direction = self.normalize_vector_to_direction(pos_delta)
        self.tail_pos = [a + b for a, b in zip(direction, self.tail_pos)]

    def normalize_vector_to_direction(self, v):
        def sign(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        return [sign(x) for x in v]
    
    def execute_part_one_instructions(self):
        for i in self.instructions:
            self.update_head(i)
            while self._tail_needs_update():
                print('head pos: ',self.head_pos,'tail pos: ', self.tail_pos)
                pass
        print(len(self.tail_position_history))
        print(len(self.rope_pos_history))




"""
Rope that's ten segments long

"""


if __name__ == "__main__":
    main()