import re
import random

"""
1. You need to predict where robots will be in the future based on their positions and velocity
2. Robots can stack on the same tile without interfering with each other
3. Robots can wrap around to the other side of the board.

Part one:
Find where robots will be after 100 seconds
Find the number of robots in each quadrant



In this example, the quadrants contain 1, 3, 4, and 1 robot. Multiplying these together gives a total safety factor of 12.

Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall. What will the safety factor be after exactly 100 seconds have elapsed?

"""
class RobotHandler():
    def __init__(self):
        self.robot_dict = self.process_file()
        self.grid_x_width = 101
        self.grid_y_height = 103
        self.total_steps = 0
        self.number_of_guards = len(self.robot_dict)
        
    def process_file(self, filename = "input.txt"):
        d = {}
        with open(filename) as file:
            for line in file:
                numbers = re.findall("[-]\d+|\d+",line) #Negative numbers exist...
                position = (int(numbers[0]), int(numbers[1]))
                velocity = (int(numbers[2]), int(numbers[3]))
                #Starting positions are not unique. Using position and velocity as unique identifier, and value is current position.
                d[(position, velocity, self.get_colour())] = position
        return d

    def get_colour(self):
        match random.randint(1,6):
            case 1:
                colour = (200,150,100)
            case 2:
                colour = (random.randint(155,255),20,20)
            case 3:
                colour = (255,255,random.randint(210,255))
            case _:
                colour = (20,random.randint(150,255),20)
        return colour

    def interesting_frame(self):
        # Midpoints of the grid
        halfway_height = self.grid_y_height // 2
        halfway_width = self.grid_x_width // 2

        # Initialize counters for each quadrant
        a = b = c = d = e = 0
        # Classify robots into quadrants, excluding the middle row/column
        for _, (current_x, current_y) in self.robot_dict.items():
            if current_x == halfway_width or current_y == halfway_height:
                # Skip robots in the middle row or column
                continue
            top_left_x = halfway_width //2
            top_left_y = halfway_height //2
            bottom_right_x = top_left_x + halfway_width
            bottom_right_y = top_left_y + halfway_height
            if current_x < halfway_width and current_y < halfway_height:  # Top-left
                a += 1
            elif current_x < halfway_width and current_y > halfway_height:  # Bottom-left
                b += 1
            elif current_x > halfway_width and current_y < halfway_height:  # Top-right
                c += 1
            elif current_x > halfway_width and current_y > halfway_height:  # Bottom-right
                d += 1
            elif current_x > top_left_x and current_x < bottom_right_x and current_y > top_left_y and current_y < bottom_right_y:
                e += 1
        target = self.number_of_guards * 0.4
        if any(x > target for x in (a,b,c,d,e)):
            return True
        else:
            return False

    def frame_has_christmas_tree(self):
        target = 30
        dx = {}
        dy = {}
        for x,y in self.robot_dict.values():
            dx[x] = dx.get(x,0) + 1
            dy[y] = dy.get(y,0) + 1
        if any(x > target for x in dx.values()) and any(x > target for x in dy.values()):
            return True
        else:
            return False

    def step_robots(self, n = 1):
        self.total_steps += n
        print(self.total_steps)
        for k, v in self.robot_dict.items():
            position, velocity, colour = k
            current_position = v
            new_x = current_position[0] + velocity[0]*n
            new_y = current_position[1] + velocity[1]*n
            if new_x >= self.grid_x_width:
                amount_over = new_x // self.grid_x_width
                new_x -= self.grid_x_width * amount_over
            if new_x < 0:
                amount_over = new_x // self.grid_x_width
                new_x -= self.grid_x_width * amount_over
            if new_y >= self.grid_y_height:
                amount_over = new_y // self.grid_y_height
                new_y -= self.grid_y_height * amount_over
            if new_y < 0:
                amount_over = new_y // self.grid_y_height
                new_y -= self.grid_y_height * amount_over
            new_position = (new_x, new_y)
            self.robot_dict[k] = new_position

    def get_final_colours(self):
        self.step_robots(6620)

    def build_robot_grid(self):
        """Don't really need this to solve anything - just for looks!"""
        l = []
        for i in range(self.grid_y_height):
            s = []
            for j in range(self.grid_x_width):
                s.append(1)
            l.append(s)
        for key, coords in self.robot_dict.items():
            position, velocity, colour = key
            x, y = coords
            ylb = 53
            yub = 85
            xlb = 51
            xub = 81
            frame_colour = (200,150,100)
            if (y == ylb or y == yub) and x >= xlb and x <= xub  and self.total_steps == 6620: #Hard coded ans for pretty picture
                colour = frame_colour
            elif (x == xlb or x ==xub) and y <= yub and y >= ylb and self.total_steps == 6620: #Hard coded ans for pretty picture
                colour = frame_colour
            elif x < xub and x > xlb and y < yub and y > ylb and self.total_steps == 6620:
                if random.randint(0,15) == 5:
                    colour = (random.randint(155,255),20,20)
                else:
                    colour = (20,random.randint(150,255),20)
            elif self.total_steps == 6620:
                colour = (215,215,random.randint(210,255))
            l[y][x] = colour
        return l

    def move_robots():
        pass
        


if __name__ == "__main__":
    x = RobotHandler()
    x.get_final_colours()
    yd = {}
    xd = {}
    for k,v in x.robot_dict.items():
        xc, yc = v
        xd[xc] = xd.get(xc,0) +1
        yd[yc] = yd.get(yc,0) +1
    print(yd,xd)