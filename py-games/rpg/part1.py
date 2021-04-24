import pygame
from pygame.locals import *
import sys
import random

pygame.init()
vec = pygame.math.Vector2

# CONSTANTS
HEIGHT = 550
WIDTH = 1000
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# CLASS INTERFACES
class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("assets/background.png")        
            self.bgY = 0
            self.bgX = 0
 
      def render(self, mainsurface):
            mainsurface.blit(self.bgimage, (self.bgX, self.bgY))
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("Ground.png")
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((26, 54, 33))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT-30))
 
    def render(self, mainsurface):
        mainsurface.blit(self.surf, (self.rect.x, self.rect.y))  
           
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Idle (1).png")
        self.rect = self.image.get_rect()
 
        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.direction = "RIGHT"
    def update(self):
        pass

    def move(self):
        pass    

    def jump(self):
        pass
     
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


# ---- GAME SETUP ----- #
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# BACKGROUND OBJECTS
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

# CHARACTER OBJECTS
player = Player()


# ---- GAME LOOP ----- #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.jump()

    player.move()
    
    background.render(display_surface)
    ground.render(display_surface)
    display_surface.blit(player.image, player.rect)

    pygame.display.update() 
    FPS_CLOCK.tick(FPS)
