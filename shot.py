import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 100, 255), self.position, self.radius, 2)
        return
    
    def move(self, dt):
        self.position += self.velocity * dt
        return
    
    def update(self, dt):
        self.move(dt)