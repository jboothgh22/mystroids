import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius
        
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def did_it_collide(self, asteroid):
        the_distance = pygame.math.Vector2.distance_to(self.position, asteroid.position)
        
        if the_distance <= (self.radius + asteroid.radius):
            return True
        
        return False