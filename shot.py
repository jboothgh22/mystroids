from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update_position(self, new_position):
        self.position = new_position
 
    def update_velocity(self, new_velocity):
        self.velocity = new_velocity   
    
    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        shot_center = self.position
        shot_rect = pygame.draw.circle(screen,
                                      color = 'white',
                                      center = shot_center,
                                      radius = self.radius,
                                      width = 2)