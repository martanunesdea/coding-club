# randomly generated platforms
import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(GREEN)
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
        condition = (self.pos.y > hits[0].rect.y + 5) 
        if hits and condition:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

    def jump(self):
        # only jump if sprite was touching the platform to begin
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15
 

class platform(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((50, 12))
            self.surf.fill((0,255,0))
            self.rect = self.surf.get_rect(center=(random.randint(0,WIDTH-10),
                                                    random.randint(0, HEIGHT-30)))
                                                
    def move(self):
        pass


# --- SETUP --- #
HEIGHT = 450
WIDTH = 400
GREEN = (128,255,40)
RED = (255,0,0)
BLACK = (0,0,0)
ACCELERATION = 0.5
ACC = 0.5
FRIC = -0.12
FPS = 60


# MAIN DISPLAY RELATED
frame_per_sec = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
vec = pygame.math.Vector2 #2 for two dimensional
 
# SPRITES
PT1 = platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

P1 = Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)
 
## generating the platforms that appear in the start of the game
for x in range(random.randint(5, 8)):
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)

# --- GAME LOOP --- #
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
         
    main_display.fill(BLACK)
    P1.move()
 
    for entity in all_sprites:
        main_display.blit(entity.surf, entity.rect)
        entity.update()
 
    pygame.display.update()
    frame_per_sec.tick(FPS)