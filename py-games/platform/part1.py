import pygame
from pygame.locals import *

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect()
   
        self.pos = vector((10, 385))
        self.vel = vector(0,0)
        self.acc = vector(0,0)
 
    def move(self):
        # resetting
        self.acc = vector(0,0)
    
        # checking what to update it to
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACCELERATION
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACCELERATION
             
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos   
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
    
# ------- SETUP -------- #
## CONSTANTS
HEIGHT = 450
WIDTH = 400
GREEN = (128,255,40)
RED = (255,0,0)
BLACK = (0,0,0)
ACCELERATION = 0.5
FRIC = -0.12
FPS = 60

## MAIN DISPLAY related
frames_per_sec = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
vector = pygame.math.Vector2 

## SPRITES
PT1 = platform()
player1 = Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(player1)
 
# ------- LOOP -------- #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # refresh main display
    main_display.fill(BLACK)
 
    # updates sprites
    player1.move()
    for entity in all_sprites:
        main_display.blit(entity.surf, entity.rect)
        entity.update()
    
    # update main display
    pygame.display.update()
    frames_per_sec.tick(FPS)