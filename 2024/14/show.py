import pygame
import sys
import main
import time

import math
import random

# Constants
TILE_SIZE = 10  # Size of each tile
GRID_WIDTH = 101
GRID_HEIGHT = 103
SCREEN_WIDTH = TILE_SIZE * GRID_WIDTH
SCREEN_HEIGHT = TILE_SIZE * GRID_HEIGHT
FPS = 60

# Colors
COLOR_MAP = {
    0: (255, 255, 255),  # White
    1: (0, 0, 45),        # Black
    2: (255, 0, 0),      # Red
    3: (0, 255, 0),      # Green
    4: (0, 0, 255),      # Blue
}

# Fireworks Manager Class
class FireworksManager:
    def __init__(self):
        self.particles = []

    def create_firework(self, x, y):
        colors = [(255, 0, 0), (255, 165, 0)]  # Red and Orange
        for _ in range(100):  # Create 100 particles per firework
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            lifetime = random.randint(40, 80)
            color = random.choice(colors)
            self.particles.append(Particle(x, y, color, angle, speed, lifetime))

    def update(self):
        # Update particles and remove those with no lifetime left
        for particle in self.particles:
            particle.update()
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)

# Particle Class for Fireworks
class Particle:
    def __init__(self, x, y, color, angle, speed, lifetime):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.speed = speed
        self.lifetime = lifetime
        self.radius = 3

    def update(self):
        # Update position based on angle and speed
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        # Reduce lifetime
        self.lifetime -= 1
        # Slow down slightly
        self.speed *= 0.98

    def draw(self, surface):
        if self.lifetime > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)


# Grid Manager Class
class GridManager:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, value in enumerate(row):
                color = COLOR_MAP.get(value, value)  # Default to light gray
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, color, rect)

    def update(self, grid):
        # Example: Cycle through colors for all tiles
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = (grid[y][x])
                
    def set_grid(self, new_grid):
        """Replace the grid with a new one."""
        if len(new_grid) == self.height and all(len(row) == self.width for row in new_grid):
            self.grid = new_grid
        else:
            raise ValueError("New grid dimensions must match the existing grid.")

# Main Game Class
class Game:
    def __init__(self):

        pygame.init()
        self.fireworks_manager = FireworksManager()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Bathroom Guards")
        self.clock = pygame.time.Clock()
        self.grid_manager = GridManager(GRID_WIDTH, GRID_HEIGHT)
        self.robot = main.RobotHandler()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_9:
                    self.run_robot_simulation()
                if event.key == pygame.K_SPACE:  # Press SPACE to update the grid
                    self.robot.step_robots()
                    new_grid = self.robot.build_robot_grid()
                    self.grid_manager.update(new_grid)
                if event.key == pygame.K_z:  # Press SPACE to update the grid
                    self.robot.step_robots(-1)
                    new_grid = self.robot.build_robot_grid()
                    self.grid_manager.update(new_grid)
                if event.key == pygame.K_x:  # Press SPACE to update the grid
                    self.robot.step_robots(27)
                    new_grid = self.robot.build_robot_grid()
                    self.grid_manager.update(new_grid)
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position and calculate grid coordinates
                mouse_x, mouse_y = event.pos
                grid_x = mouse_x // TILE_SIZE
                grid_y = mouse_y // TILE_SIZE
                print(f"Grid cell clicked: ({grid_x}, {grid_y})")


    def run_robot_simulation(self):
        """Run robot simulation while allowing the screen to update."""
        self.robot.step_robots(-self.robot.total_steps)
        christmas_frame = False

        while not christmas_frame:
            # Process events to avoid freezing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return  # Exit simulation if the user quits

            # Update robot positions
            if self.robot.total_steps < 6600:
                self.robot.step_robots(50)
            else:
                self.robot.step_robots()
            christmas_frame = self.robot.frame_has_christmas_tree()

            # Update the grid
            new_grid = self.robot.build_robot_grid()
            self.grid_manager.update(new_grid)

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Draw the grid
            self.grid_manager.draw(self.screen)

            # Refresh the display
            pygame.display.flip()

        # Trigger multiple sequential fireworks
        for i in range(25):  # Launch 5 fireworks
            self.fireworks_manager.create_firework(
                random.randint(100, SCREEN_WIDTH - 100),  # Random x position
                random.randint(100, SCREEN_HEIGHT - 100)  # Random y position
            )

            for _ in range(30):  # Display each firework for 0.5 seconds (30 frames at 60 FPS)
                self.handle_events()  # Allow quitting during fireworks
                self.fireworks_manager.update()

                # Clear the screen
                self.screen.fill((0, 0, 0))

                # Draw the grid and fireworks
                self.grid_manager.draw(self.screen)
                self.fireworks_manager.draw(self.screen)

                # Refresh the display
                pygame.display.flip()
                self.clock.tick(FPS)

            # Short delay between fireworks
            # time.sleep(0.5)

        

    def run(self):
        while self.running:
            self.handle_events()

            # Clear the screen
            self.screen.fill((0, 0, 0))

            # Draw the grid
            self.grid_manager.draw(self.screen)

            # Refresh the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
