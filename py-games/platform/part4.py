# scrolling background
import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
 
    def move(self):
        self.acc = vec(0,0.5)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        #if P1.vel.y > 0:        
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    def jump(self):
        #hits = pygame.sprite.spritecollide(self, platforms, False)
        #if hits:
        self.vel.y = -15
 
 
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
    def move(self):
        pass


# --- SETUP ---- #
HEIGHT = 450
WIDTH = 400
GREEN = (128,255,40)
RED = (255,0,0)
BLACK = (0,0,0)
ACCELERATION = 0.5
ACC = 0.5
FRIC = -0.12
FPS = 60

## MAIN DISPLAY related
frames_per_sec = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
vector = pygame.math.Vector2 

## SPRITES
PT1 = platform()
P1 = Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)

def plat_generation(x_coord, y_coord):
    p = platform()
    p.surf = pygame.Surface((80, 10))
    p.surf.fill((255,0,0))
    p.rect = p.surf.get_rect(center = (x_coord, y_coord))
    return p

PT2 = plat_generation(WIDTH/2, HEIGHT - (HEIGHT/3))
PT3 = plat_generation(WIDTH/2, HEIGHT/3)
PT4 = plat_generation(WIDTH/2, HEIGHT/6)

platforms.add(PT2)
all_sprites.add(PT2)
platforms.add(PT3)
all_sprites.add(PT3)
platforms.add(PT4)
all_sprites.add(PT4)
 

# ------- LOOP -------- #
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()

    # refresh main display
    main_display.fill(BLACK)
    P1.move()
 
    # updates sprites
    for entity in all_sprites:
        main_display.blit(entity.surf, entity.rect)
        entity.update()
 
    # infinite scrolling
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y) # update player
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y) # update platforms
            if plat.rect.top >= HEIGHT:
                plat.kill() # destroy platforms out of screen

    # update main display
    pygame.display.update()
    frames_per_sec.tick(FPS)