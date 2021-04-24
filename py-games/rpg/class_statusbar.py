import pygame
from pygame.locals import *

HEIGHT = 600
WIDTH = 800
# light shade of the button 
color_light = (170,170,170)
color_dark = (100,100,100)
color_white = (255,255,255) 

class StatusBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((150, 60))
        self.rect = self.surf.get_rect(center = (500, 10))
        self.surf.fill((255,255,255))
    
    def display(self, display_surface):
        display_surface.blit(self.surf, (600,5))

    def update_draw(self, font, level, enemies, exp, display_surface):
        # Create the text to be displayed
        text1 = font.render("LEVEL: " + str(level), True , color_dark)
        text2 = font.render("ENEMIES DESTRYED: " + str(enemies), True, color_dark)
        text3 = font.render("EXP: " + str(exp), True, color_dark)

        # Draw the text to the status bar
        display_surface.blit(text1, (610, 10))
        display_surface.blit(text2, (610, 30))
        display_surface.blit(text3, (610, 50))


       