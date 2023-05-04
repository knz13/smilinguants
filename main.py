from src.general import *
from src.ant import *

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smilinguants")

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw game objects
    # ...

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()



