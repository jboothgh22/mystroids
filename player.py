from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shot_timer = 0



    # in the player class this is the ship's shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        my_points = self.triangle()
        my_rect = pygame.draw.polygon(surface = screen, 
                                      color = "white",
                                      points = my_points,
                                      width = 2 )
        
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def move(self, dt):
        movevect = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += movevect*PLAYER_SPEED*dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def shoot(self, dt):
        if self.shot_timer <= 0:
            new_shot = Shot(self.position[0], self.position[1])
            velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOT_SPEED
    
            new_shot.update_velocity(velocity)
            self.shot_timer = 0.3
        else:
            self.shot_timer -= dt




