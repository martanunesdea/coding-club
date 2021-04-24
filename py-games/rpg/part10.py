# health bar
# collision detection 1
import pygame
from pygame.locals import *
import sys
import random
from class_background import *
from class_player import *
from class_enemy import *
from class_healthbar import *
from class_statusbar import *
from class_collectible import *


pygame.init()  # Begin pygame
vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 800
ACC = 0.5
FRIC = -0.1
JUMP = -7
GRAVITY = 0.25
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

# ---- GAME SETUP ----- #
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


# BACKGROUND OBJECTS
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
health = HealthBar()
status_bar = StatusBar()
item = Item(1)
Items = pygame.sprite.Group()
Items.add(item)
# CHARACTER OBJECTS
player = Player()
enemy = Enemy()
player_group = pygame.sprite.Group()
player_group.add(player)

# FONTS
headingfont = pygame.font.SysFont('Verdana', 40)
regularfont = pygame.font.SysFont('Corbel',25)
smallerfont = pygame.font.SysFont('Corbel',16) 

hit_cooldown = pygame.USEREVENT + 1

# ---- LOOP ----- #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        if event.type == pygame.MOUSEBUTTONDOWN:
              pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.jump(ground_group)
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True  

        if event.type == hit_cooldown:
            player.cooldown = False

    # Updating player
    player.move()
    enemy.move()
    player.update()
    
    if player.attacking == True:
        player.attack() 
    
    enemy.update(player, player_group, hit_cooldown)
    player.gravity_check(ground_group)

    for i in Items:
        i.render(display_surface)
        i.update(player, player_group, health)

    # Updating objects on main display
    background.update()
    background.render(display_surface)
    ground.render(display_surface)
    health.render(player, display_surface)
    player.render(display_surface)
    enemy.render(display_surface)

    status_bar.display(display_surface)
    level = 1
    enemies = 10
    exp = 0
    status_bar.update_draw(smallerfont, level, enemies, exp, display_surface)

    # Updating main display
    pygame.display.update() 
    FPS_CLOCK.tick(FPS)
