import pygame

#base class for game objects (player and asteroid)

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
            
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def draw(self, screen):
        #implementations must override
        pass
    
    def update(self, dt):
        #implementations must override
        pass
<<<<<<< HEAD
    
    def hit_check(self, target):
        distance = pygame.math.Vector2(self.position).distance_to(target.position)
        return distance < self.radius + target.radius
=======
    
>>>>>>> 6888355 (Created and drew player)
