import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)
        return
    
    def move(self, dt):
        self.position += self.velocity * dt
        return
    
    def update(self, dt):
        self.move(dt)