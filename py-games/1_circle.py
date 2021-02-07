# Simple pygame program
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the main display
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

# Run until the user asks to quit
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    color = (0, 0, 255)
    coordinates = (250, 250)
    diameter = 75
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, color, coordinates, diameter)

    # Flip the display
    pygame.display.flip()

