import pygame
from constants import *

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.length = 1
        self.color = SNAKE_COLOR
        self.grow_pending = False

    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.length = 1
        self.grow_pending = False

    def turn(self, direction):
        if self.length > 1 and (direction[0] * -1, direction[1] * -1) == self.direction:
            return
        self.direction = direction

    def move(self):
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        if new_head in self.positions:
            return False

        self.positions.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
            self.length += 1
        else:
            self.positions.pop()

        return True

    def grow(self):
        self.grow_pending = True
        self.length += 1

    def draw(self, surface):
        for i, pos in enumerate(self.positions):
            color = self.color if i == 0 else DARK_GREEN
            rect = pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, DARK_GREEN, rect, 1)

    def handle_key(self, key):
        if key == pygame.K_UP or key == pygame.K_w:
            self.turn(UP)
        elif key == pygame.K_DOWN or key == pygame.K_s:
            self.turn(DOWN)
        elif key == pygame.K_LEFT or key == pygame.K_a:
            self.turn(LEFT)
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            self.turn(RIGHT)
