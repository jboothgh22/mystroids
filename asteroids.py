import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        #self.velocity = random.randint(-20, 20)
        

    def draw(self, screen):
        ast_center = self.position
        ast_rect = pygame.draw.circle(screen,
                                      color = 'white',
                                      center = ast_center,
                                      radius = self.radius,
                                      width = 2)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):

        original_size = self.radius
        self.kill()

        if original_size <= ASTEROID_MIN_RADIUS:
            return 0
        else:
            new_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid1.velocity = self.velocity.rotate(new_angle)*1.2
            new_asteroid2.velocity = self.velocity.rotate(-new_angle)*1.2


        



