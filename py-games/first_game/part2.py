# With collision detection
import pygame, sys
from pygame.locals import *
import random, time # now also importing time for timer functions
 

### GAME SETUP #############
pygame.init()

# Game constants
GAME_NAME = "Dodge The Enemy"
FPS = 60
RED   = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
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
            global SCORE
            self.rect.top = 0
            self.rect.center = (random.randint(40, (SCREEN_WIDTH-40)), 0)
            SCORE = SCORE + 1
            print("SCORE IS: ", SCORE)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/rocket.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center = (200, 500))      
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     

### GAME STARTUP ############## 
# Create main Surface
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption(GAME_NAME)

# Create FPS object
FramePerSec = pygame.time.Clock()

# Create Sprites
P1 = Player()
E1 = Enemy()

# Create Sprites groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

### GAME LOOP ##############
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update background of display
    DISPLAYSURF.fill(WHITE)

    # update sprite groups
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # detect collision
    if pygame.sprite.spritecollideany(P1, enemies):
          DISPLAYSURF.fill(RED)
          pygame.display.update()
          time.sleep(1)
          pygame.quit() # quit pygame
          sys.exit()    # closing the window
    
    pygame.display.update()
    FramePerSec.tick(FPS)