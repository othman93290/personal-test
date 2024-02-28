import pygame
import random

class Snake:
    def __init__(self, width, height, grid_size):
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.length = 1
        self.positions = [((width // 2), (height // 2))]
        # Assurez-vous que self.direction est un tuple
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.color = (0, 255, 0)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * self.grid_size)) % self.width), (cur[1] + (y * self.grid_size)) % self.height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((self.width // 2), (self.height // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (self.grid_size, self.grid_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 0, 255), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))
                    
    def head_collides_with_body(self):
        return self.positions[0] in self.positions[1:]