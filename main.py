import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Initialize pygame
pygame.init()

dt = 0

mystroids_clock = pygame.time.Clock()

# Create groups of objects
updateable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
asteroid_group = pygame.sprite.Group()
shot_group = pygame.sprite.Group()

# Create the containers for the object groups
Player.containers = (updateable_group, drawable_group)
Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
AsteroidField.containers = (updateable_group)
Shot.containers = (updateable_group, drawable_group, shot_group)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

my_a_field = AsteroidField()

my_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
# Start an infinite while loop:
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
     
    delta_time = mystroids_clock.tick(60)
    dt = delta_time/1000

    # Draw black window
    screen.fill(color = (0,0,0))
   
   
    # Update player and asteroid motion
    for thing in updateable_group:
        thing.update(dt)
        

    # Draw the player and asteroids
    for thing in drawable_group:
        thing.draw(screen)

    
    for thing in asteroid_group:
        answer = my_player.did_it_collide(thing)

        if answer == True:
            print(f"Game Over!")
            exit(100)

    for aster_thing in asteroid_group:
        for shot_thing in shot_group:

            answer = shot_thing.did_it_collide(aster_thing)

            if answer == True:
                shot_thing.kill()
                aster_thing.split()

    # Render the screen
    pygame.display.flip()
    
    

 

if __name__ == "__main__":
    main()
