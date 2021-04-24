import pygame, sys
from pygame.locals import *
import random
 
#### GAME SETUP ######
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining game constants
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GAME_NAME = "Dodge The Enemy"
SCORE = 0
# Creating the main surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption(GAME_NAME)

# Create class interfaces
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/alien.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center = (random.randint(40, (SCREEN_WIDTH-40)),0))     
 
      def move(self):
        self.rect.move_ip(0,5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, (SCREEN_WIDTH-40)), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # initilizing Sprite 
        self.image = pygame.image.load("images/rocket.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center = (250, 500))      
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
      

### GAME STARTUP #######
P1 = Player()
E1 = Enemy()

while True:     
    list_events = pygame.event.get()
    
    for event in list_events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # get physical updates
    P1.update()
    E1.move()
    # update graphics
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF) 
    E1.draw(DISPLAYSURF)
    
    pygame.display.update()
    FramePerSec.tick(FPS)