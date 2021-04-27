# randomly generated platforms - continuously
import pygame
from pygame.locals import *
import sys
import random
 
pygame.init()

# CLASS INTERFACES
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
        if hits:
            if self.vel.y > 0:
                if (self.pos.y) < hits[0].rect.bottom:              
                    self.pos.y = hits[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False

    def jump(self):
        #hits = pygame.sprite.spritecollide(self, platforms, False)
        #if hits:
        self.vel.y = -11
 
 
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((random.randint(50,100), 12))
            self.surf.fill((0,255,0))
            self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                    random.randint(0, HEIGHT-30)))

    def move(self):
        pass 

def platform_generation():
    while len(platforms) < 10:
        width = random.randrange(50,100)    # declare random width
        p  = platform()                     # create new platform object
        # give new platform random coordinates
        p.rect.center = (random.randrange(0, WIDTH - width), random.randrange(-55, 0))
        
        # add new platform to sprite groups
        platforms.add(p)
        all_sprites.add(p)

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
FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
vec = pygame.math.Vector2 #2 for two dimensional

# base platform
PT1 = platform()
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

P1 = Player()
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)
 
## generating the platforms that appear in the start of the game
for x in range(random.randint(7, 9)):
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
         
    displaysurface.fill((0,0,0))
    P1.move()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.update()
 
    # infinite scrolling
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y = P1.pos.y + abs(P1.vel.y) # update player
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y) # update platforms
            if plat.rect.top >= HEIGHT:
                plat.kill() # destroy platforms out of screen
    platform_generation()  # generate new platforms if needed

    pygame.display.update()
    FramePerSec.tick(FPS)