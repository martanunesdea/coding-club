import pygame
from pygame.locals import *
import random

HEIGHT = 600
WIDTH = 800
ACC = 0.5
FRIC = -0.1
JUMP = -7
GRAVITY = 0.25
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
vec = pygame.math.Vector2

class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/health_five.png")
 
    def render(self, player, display_surface):
        if player.lives == 5:
            self.image = pygame.image.load("assets/health_five.png")
        elif player.lives == 4:
            self.image = pygame.image.load("assets/health_four.png")
        elif player.lives == 3:
            self.image = pygame.image.load("assets/health_three.png")
        elif player.lives == 2:
            self.image = pygame.image.load("assets/health_two.png")
        elif player.lives == 1:
            self.image = pygame.image.load("assets/health_one.png")
        elif player.lives == 0:
            self.image = pygame.image.load("assets/health_zero.png")
        
        display_surface.blit(self.image, (10,10))          
