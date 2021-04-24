import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center = (10, 420))
        self.pos = vec((30, 30))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,GRAVITY)  # changing from 0 will activate gravity
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACCELERATION
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACCELERATION 

        self.acc.x = self.acc.x + (self.vel.x * FRIC)
        self.vel = self.vel + self.acc
        self.pos = self.pos + (self.vel + 0.5 * self.acc)

        self.rect.midbottom = self.pos

    #def update(self):
        #hits = pygame.sprite.spritecollide(player1, platform, False)
        #if hits:
            # the hits[0] is to refer to the player1 sprite
            # so hits[0].rect.top is getting the top coordinates of the rect of player1
            #self.pos.y = hits[0].rect.top + 1
           # self.vel.y = 0


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
GRAVITY = 0.1
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

platforms = pygame.sprite.Group()
platforms.add(PT1)
 
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
