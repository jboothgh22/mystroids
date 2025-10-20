import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Start an infinite while loop:
while(1):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
     
    screen.fill(color = (0,0,0))
    pygame.display.flip()

 

if __name__ == "__main__":
    main()
