import pygame
from pygame.locals import *
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))
        self.pos = vec((30, 30))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0.1)  # changing from 0 will activate gravity
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(player1, platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0   

    def jump(self):
        self.vel.y = -15
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

# ------- SETUP -------- #
HEIGHT = 450
WIDTH = 400
GREEN = (128,255,40)
RED = (255,0,0)
BLACK = (0,0,0)
ACCELERATION = 0.5
ACC = 0.5
FRIC = -0.12
FPS = 60

# MAIN DISPLAY related
FramePerSec = pygame.time.Clock()
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# SPRITES
PT1 = platform()
player1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(player1)
platforms = pygame.sprite.Group()
platforms.add(PT1)
 
# --- GAME LOOP --- #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
     
    # refresh screen
    main_display.fill(BLACK)
 
    # update sprites
    player1.move()
    for entity in all_sprites:
        main_display.blit(entity.surf, entity.rect)
        entity.update()
 
    # update main display
    pygame.display.update()
    FramePerSec.tick(FPS)
