# score
# game over screen
import pygame
from pygame.locals import *
import sys
import random, time
 
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional
 
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.score = 0
 
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
   
        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
           self.jumping = True
           self.vel.y = -15
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def update(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if hits:
            # this can be tweaked for better graphics
            if (self.pos.y) < hits[0].rect.bottom: 
                # check if the platform can give point (true), if so, add to score and set platform to false
                if hits[0].point == True:   
                        self.score += 1
                        hits[0].point = False  
                self.pos.y = hits[0].rect.top +1
                self.vel.y = 0
                self.jumping = False
 
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((random.randint(50,100), 12))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10),
                                                 random.randint(0, HEIGHT-30)))
        self.point = True
 
    def move(self):
        pass

def plat_gen():
    while len(platforms) < 10 :
        width = random.randrange(50,100)    # declare random width
        p  = platform()                     # create new platform object
        # give new platform random coordinates
        p.rect.center = (random.randrange(0, WIDTH - width),
                             random.randrange(-55, 0))
        # add new platform to sprite groups
        platforms.add(p)
        all_sprites.add(p)

        
PT1 = platform()
P1 = Player()
 
PT1.surf = pygame.Surface((WIDTH, 20))
PT1.surf.fill((255,0,0))
PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
platforms = pygame.sprite.Group()
platforms.add(PT1)
 
for x in range(random.randint(7,9)):
    pl = platform()
    pl = platform()
    platforms.add(pl)
    all_sprites.add(pl)

font = pygame.font.SysFont("Verdana", 20)     ##

while True:
    P1.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYUP:    
            if event.key == pygame.K_SPACE:
                P1.cancel_jump()  
 
    displaysurface.fill((0,0,0))
    score  = font.render(str(P1.score), True, (123,255,0))
    displaysurface.blit(score, (WIDTH/2, 10))  
    # update all sprites
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()
    
    # infinite scrolling
    if P1.rect.top <= HEIGHT / 3:
        P1.pos.y += abs(P1.vel.y) # update player
        for plat in platforms:
            plat.rect.y += abs(P1.vel.y) # update platforms
            if plat.rect.top >= HEIGHT:
                plat.kill() # destroy platforms out of screen
    plat_gen() # generate new platforms if needed

    # check if game is over
    if P1.rect.top > HEIGHT:
        for entity in all_sprites:
            entity.kill()
            time.sleep(1)
            displaysurface.fill((255,0,0))
            pygame.display.update()
            time.sleep(1)
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)