# Simple pygame program
# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the main display
screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))


blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
coordinates = (250, 250)
diameter = 75
# Draw a solid blue circle in the center
pygame.draw.circle(screen, blue, coordinates, diameter)

number = 0
# Run until the user asks to quit
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    number = number + 1

    if number % 2:
        pygame.draw.circle(screen, blue, coordinates, diameter)
    else:
        pygame.draw.circle(screen, red, coordinates, diameter)
    pygame.time.delay(1000)
    
    # Flip the display
    pygame.display.flip()

