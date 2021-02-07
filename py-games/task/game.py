import pygame
from pygame.locals import *
import sys
 
pygame.init()
 
main_surface = pygame.display.set_mode((300, 300))
main_surface.fill((0,0,0))
surface_small = pygame.Surface((50, 10))
surface_small.fill((200,0,0))
coord_x = 50
coord_y = 50

def background():
    main_surface.blit(surface_small, (coord_x,coord_y))
    main_surface.blit(surface_small, (coord_x+110,coord_y+10))

    main_surface.blit(surface_small, (coord_x+150,coord_y+50))

    main_surface.blit(surface_small, (coord_x-30,coord_y+100))
    main_surface.blit(surface_small, (coord_x+70,coord_y+120))
    main_surface.blit(surface_small, (coord_x+150,coord_y+145))

    main_surface.blit(surface_small, (coord_x-40,coord_y+210))
    main_surface.blit(surface_small, (coord_x+80,coord_y+220))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((0,70,170))
        self.rect = self.surf.get_rect(center=(150, 255))
    def draw(self, surface):
        surface.blit(self.surf, self.rect) 
        
P1 = Player()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    background()
    P1.draw(main_surface)
    pygame.display.update()