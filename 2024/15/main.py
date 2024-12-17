
class Robot():
    def __init__(self):
        self.file = self.process_file()


    def process_file(self):
        l = []
        with open("input.txt") as file:
            for i, line in enumerate(file):
                temp_list = []
                for j, char in enumerate(line.strip()):
                    temp_list.append(char)
                    if char == "@":
                        self.robot_pos = (i, j)
                # l.append(line.strip())
        return l

    def build_map(self):
        
        pass


    def main():
        pass


    # Robot = @






if __name__ == "__main__":
    x = input("t for test m for main")
    match x:
        case 't':
            print("hey")
        case 'm': 
            print("hey2")