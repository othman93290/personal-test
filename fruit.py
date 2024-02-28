import pygame
import random

class Fruit:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, self.width // self.grid_size - 1) * self.grid_size, 
                         random.randint(0, self.height // self.grid_size - 1) * self.grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (self.grid_size, self.grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (0, 0, 255), r, 1)
