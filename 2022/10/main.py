


class CPU():
    def __init__(self) -> None:
        self.instruction_set = self.process_file()
        self.cycles = 0
        self.x = 1
        self.signal_strength_data = []
        self.screen = [[x for x in range(40)] for x in range(6)]

    def process_file(self):
        l = []
        with open("input.txt") as file:
            for line in file:
                l.append(line.strip())
        return l

    def do_a_little_cycle(self, n = 1):
        if n < 0:
            return
        for _ in range(n):
            self.cycles += 1
            self.draw_pixel()
            if self.cycles % 40 == 20:
                sig_str = self.x * self.cycles
                self.signal_strength_data.append((self.cycles, self.x, sig_str))

    def draw_pixel(self):
        row = (self.cycles-1) // 40
        col = (self.cycles-1) % 40
        if col >= self.x - 1 and col <= self.x +1:
            char = "#"
        else:
            char = "."
        self.screen[row][col] = char

    def process_instruction(self, instruction:str):
        if instruction.startswith('noop'):
                self.do_a_little_cycle(1)
        else:
            a, b = instruction.split(' ')
            self.do_a_little_cycle(2)
            self.x += int(b)


    def solve_part_one(self):
        for line in self.instruction_set:
            self.process_instruction(line)
        score = 0
        for i in self.signal_strength_data:
            score += i[-1]
            print(i)
        print(score)

def main():
    x = CPU()
    x.solve_part_one()
    for row in x.screen:
        print(''.join(row))
    # print(x.screen)

if __name__ == "__main__":
    main()

    """
    CPU has a single register
    Clock circuit tickets at a constant rate; Each tick is called a cycle
    

    Two operations:
    addx V takes 2 cycles; then X register is increased by V (can be neg)
    noop takes one cycle and does nothing

    
    Part Two:
    X register controls horizontal position of a sprite
    3 pixels wide
    X register sets the horizontal position of the middle of that sprite (no vertical position exists)
    40 wide and 6 high

    CRT draws top row left to right, then the row below that, etc.

    Left most pixel in each row is position 0, right most is position 39

    CRT draws a single pixel DURING each cycle
    


    """