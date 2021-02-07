import pygame
from pygame.locals import *
import sys
 
pygame.init()
 
main_surface = pygame.display.set_mode((300, 300))
 
surface_small = pygame.Surface((50, 50))
surface_small.fill((200,100,0))
 
surface_large = pygame.Surface((100, 50))
surface_large.fill((100,0,200))

coord_x = 50
coord_y = 50
OFFSET = 100

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    main_surface.blit(surface_small, (coord_x,coord_y))
    main_surface.blit(surface_large, (coord_x,coord_y+OFFSET))
 
    pygame.display.update()