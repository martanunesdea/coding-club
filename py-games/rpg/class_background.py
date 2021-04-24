import pygame
from pygame.locals import *
import random

# Attack animation for the RIGHT
attack_ani_R = [pygame.image.load("assets/Attack (1).png"), pygame.image.load("assets/Attack (2).png"),
                pygame.image.load("assets/Attack (3).png"),pygame.image.load("assets/Attack (4).png"),
                pygame.image.load("assets/Attack (5).png"),pygame.image.load("assets/Attack (6).png"),
                pygame.image.load("assets/Attack (7).png"),pygame.image.load("assets/Attack (8).png"),
                pygame.image.load("assets/Attack (9).png"),pygame.image.load("assets/Attack (10).png")]

# Attack animation for the LEFT
attack_ani_L = [pygame.image.load("assets/Attack Left(1).png"), pygame.image.load("assets/Attack Left(2).png"),
                pygame.image.load("assets/Attack Left(3).png"),pygame.image.load("assets/Attack Left(4).png"),
                pygame.image.load("assets/Attack Left(5).png"),pygame.image.load("assets/Attack Left(6).png"),
                pygame.image.load("assets/Attack Left(7).png"),pygame.image.load("assets/Attack Left(8).png"),
                pygame.image.load("assets/Attack Left(9).png"),pygame.image.load("assets/Attack Left(10).png")]


# Run animation for the RIGHT
run_R = [pygame.image.load("assets/Run (1).png"), pygame.image.load("assets/Run (2).png"),
             pygame.image.load("assets/Run (3).png"),pygame.image.load("assets/Run (4).png"),
             pygame.image.load("assets/Run (5).png"),pygame.image.load("assets/Run (6).png"),
             pygame.image.load("assets/Run (7).png"),pygame.image.load("assets/Run (8).png"),
             pygame.image.load("assets/Run (9).png"),pygame.image.load("assets/Run (10).png") ]

# Run animation for the LEFT
run_L = [pygame.image.load("assets/Run Left (1).png"), pygame.image.load("assets/Run Left (2).png"),
             pygame.image.load("assets/Run Left (3).png"),pygame.image.load("assets/Run Left (4).png"),
             pygame.image.load("assets/Run Left (5).png"),pygame.image.load("assets/Run Left (6).png"),
             pygame.image.load("assets/Run Left (7).png"),pygame.image.load("assets/Run Left (8).png"),
             pygame.image.load("assets/Run Left (9).png"),pygame.image.load("assets/Run Left (10).png") ]

HEIGHT = 600
WIDTH = 800

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bgimage = pygame.image.load("assets/background.png") 
        self.rect_bg_img = self.bgimage.get_rect() 

        self.bgX1 = 0
        self.bgX2 = self.rect_bg_img.width
        self.moving_speed = 1

    def update(self):
        self.bgX1 = self.bgX1 - self.moving_speed
        self.bgX2 = self.bgX2 - self.moving_speed

        if self.bgX1 <= -self.rect_bg_img.width:
            self.bgX1 = self.rect_bg_img.width
        if self.bgX2 <= -self.rect_bg_img.width:
            self.bgX2 = self.rect_bg_img.width
            
    def render(self, mainsurface):
        mainsurface.blit(self.bgimage, (self.bgX1, self.bgY1))
        mainsurface.blit(self.bgimage, (self.bgX2, self.bgY2))
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("Ground.png")
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((26, 54, 33))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT-30))
 
    def render(self, mainsurface):
        mainsurface.blit(self.surf, (self.rect.x, self.rect.y))  
