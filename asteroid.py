import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(split_angle)
        vel2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2
