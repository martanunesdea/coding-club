import pygame
from pygame.locals import *
import sys
import random, time

pygame.init()
vec = pygame.math.Vector2

# CONSTANTS
HEIGHT = 550
WIDTH = 1000
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
GRAVITY = 0.2
ACC = 0.5
FRIC = -0.1
JUMPING_VELOCITY = -8
#ATTACK_DISTANCE = 200
PLAYER_HEALTH = 5
ENEMY_HEALTH = 1
ENEMY_KILLED_X = 0
ENEMY_KILLED_Y = 0
# Run animation for the RIGHT
run_R = [pygame.image.load("assets/Run (1).png"), pygame.image.load("assets/Run (2).png"),
     pygame.image.load("assets/Run (3).png"),pygame.image.load("assets/Run (4).png"),
     pygame.image.load("assets/Run (5).png"),pygame.image.load("assets/Run (6).png"),
     pygame.image.load("assets/Run (7).png"),pygame.image.load("assets/Run (8).png"),
     pygame.image.load("assets/Run (9).png"),pygame.image.load("assets/Run (10).png") ]
# Run animation for the LEFT
run_L = [pygame.image.load("assets/Run Left (1).png"), pygame.image.load("assets/Run Left (2).png"),
     pygame.image.load("assets/Run Left (3).png"),pygame.image.load("assets/Run Left (4).png"),
     pygame.image.load("assets/Run Left (5).png"),pygame.image.load("assets/Run Left (6).png"),
     pygame.image.load("assets/Run Left (7).png"),pygame.image.load("assets/Run Left (8).png"),
     pygame.image.load("assets/Run Left (9).png"),pygame.image.load("assets/Run Left (10).png") ]
# Attack animation for the RIGHT
attack_R = [pygame.image.load("assets/Attack (1).png"), pygame.image.load("assets/Attack (2).png"),
        pygame.image.load("assets/Attack (3).png"),pygame.image.load("assets/Attack (4).png"),
        pygame.image.load("assets/Attack (5).png"),pygame.image.load("assets/Attack (6).png"),
        pygame.image.load("assets/Attack (7).png"),pygame.image.load("assets/Attack (8).png"),
        pygame.image.load("assets/Attack (9).png"),pygame.image.load("assets/Attack (10).png")]
# Attack animation for the LEFT
attack_L = [pygame.image.load("assets/Attack Left(1).png"), pygame.image.load("assets/Attack Left(2).png"),
        pygame.image.load("assets/Attack Left(3).png"),pygame.image.load("assets/Attack Left(4).png"),
        pygame.image.load("assets/Attack Left(5).png"),pygame.image.load("assets/Attack Left(6).png"),
        pygame.image.load("assets/Attack Left(7).png"),pygame.image.load("assets/Attack Left(8).png"),
        pygame.image.load("assets/Attack Left(9).png"),pygame.image.load("assets/Attack Left(10).png")]

run_animation_step = 0

# CLASS INTERFACES
class Background(pygame.sprite.Sprite):
      def __init__(self):
            super().__init__()
            self.bgimage = pygame.image.load("assets/background.png")        
            self.bgY = 0
            self.bgX = 0
 
      def render(self, mainsurface):
            mainsurface.blit(self.bgimage, (self.bgX, self.bgY))
 
class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load("Ground.png")
        self.surf = pygame.Surface((WIDTH, 50))
        self.surf.fill((26, 54, 33))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT-30))
 
    def render(self, mainsurface):
        mainsurface.blit(self.surf, (self.rect.x, self.rect.y))  
           
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Idle (1).png")
        self.rect = self.image.get_rect()
 
        # Position and direction
        self.vx = 0
        self.pos = vec((340, 240))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.direction = "RIGHT"
        self.right = True
        self.left = False
        self.health = PLAYER_HEALTH
        self.attacking = False
        self.attack_frame = 0
        self.cooldown = False
    def touching_ground(self):
        hits = pygame.sprite.spritecollide(player , ground_group, False)
        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0   
                
    def jump(self):
        hits = pygame.sprite.spritecollide(player , ground_group, False)
        if hits:
            self.vel.y = JUMPING_VELOCITY

    def move(self):


        self.acc = vec(0,GRAVITY)  
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > 0:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT] and self.rect.right < WIDTH:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

    def run_animation(self):

        global run_animation_step
        if abs(self.vel.x) > 1:
            self.running = True
        else:
            self.running = False


        if self.vel.x > 0:
            self.right = True
            self.left = False
        elif self.vel.x < 0:
            self.left = True
            self.right = False


        if self.running == True and self.left:
            run_animation_step += 1
            self.image = run_L[run_animation_step]
        elif self.running == True and self.right:
            run_animation_step += 1
            self.image = run_R[run_animation_step]
#idle
        elif self.running == False and self.right:
            self.image = pygame.image.load("assets/Idle (1).png")
        else:
            self.image = pygame.image.load("assets/Idle (1) Left.png")
        if run_animation_step + 1 >= 10:
            run_animation_step = 0
    def attack(self):
        self.attack_frame += 1
        if self.attacking == True and self.left:
            self.image = attack_L[self.attack_frame]
        elif self.attacking == True and self.right:
            self.image = attack_R[self.attack_frame]
#idle

        if self.attack_frame + 1 >= 10:
            self.attack_frame = 0
            player.attacking = False
    def enemy_collision(self):
        if not self.cooldown:

            hits = pygame.sprite.spritecollide(player , enemy_group, False)
            if hits and not self.attacking and self.vel.y < 1:
                self.health = self.health - 1
                self.cooldown = True
            if hits and self.attacking:
                hits[0].health = hits[0].health - 1
                #print(str(hits[0].health))
                self.cooldown = True
            if hits and self.vel.y > 0:
                hits[0].health = hits[0].health - 1
                self.vel.y = JUMPING_VELOCITY
                self.acc.y = 0
            if hits:
                pygame.time.set_timer(cooldown_timer, 3000)
                print(str(hits[0].health))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect(center = (random.randint(50 ,WIDTH-30),HEIGHT - 50))

        # Position and direction
        self.death_message = False
        self.pos = vec((self.rect.x, self.rect.y))
        self.vel = vec(5,0)
        self.acc = vec(0,0)
        self.right = True
        self.left = False
        self.health = ENEMY_HEALTH
    def move(self):
        self.pos = self.pos + self.vel
        self.rect.center = self.pos
        if self.pos.x >= WIDTH or self.pos.x <= 0:
            self.vel.x = self.vel.x * -1
class HealthBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/health_five.png")
        self.x = 10
        self.y = 10

    def render(self, mainsurface):
        if player.health == 4:
            self.image = pygame.image.load("assets/health_four.png")
        if player.health == 3:
            self.image = pygame.image.load("assets/health_three.png")
        if player.health == 2:
            self.image = pygame.image.load("assets/health_two.png")
        if player.health == 1:
            self.image = pygame.image.load("assets/health_one.png")
        if player.health <= 0:
            self.image = pygame.image.load("assets/health_zero.png")
        mainsurface.blit(self.image, (self.x, self.y))  

"""
class Attack(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((ATTACK_DISTANCE, 100))
        self.surf.fill((26, 54, 32))
        self.rect = self.surf.get_rect(center = (player.pos.x, player.pos.y))
 
    def update(self):
        if player.left:
            self.rect = self.surf.get_rect(center = (player.pos.x - 25, player.pos.y-50))
        elif player.right:
            self.rect = self.surf.get_rect(center = (player.pos.x + 25, player.pos.y-50))
        else:
            pass
    
    def attack(self):
        hits = pygame.sprite.spritecollide(attack, enemy_group, False)
        if hits:
            enemy.health = enemy.health - 1
"""
# ---- GAME SETUP ----- #
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Game")

cooldown_timer = pygame.USEREVENT + 1
death_message_timer = pygame.USEREVENT + 2
font = pygame.font.SysFont("Verdana", 30)
death_message_cond = False
# BACKGROUND OBJECTS
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)
enemy_killed_msg = font.render("Enemy Killed!", True, (0,0,0))
# CHARACTER OBJECTS
player = Player()
enemy = Enemy()
Health = HealthBar()
#attack = Attack()
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)
all_characters = pygame.sprite.Group()
all_characters.add(enemy)
all_characters.add(player)
dead_group = pygame.sprite.Group()
enemy_num = 1
def enemy_generation():
    while len(enemy_group) == 0:
        global enemy_num
        enemy_num += 1
        for x in range(1,enemy_num):
            enemy = Enemy()
            enemy_group.add(enemy)
            all_characters.add(enemy)
# ---- GAME LOOP ----- #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
             
        if event.type == cooldown_timer:
            player.cooldown = False

        if event.type == death_message_timer:
            death_message_cond = False
        
        # Event handling for a range of different key presses    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    player.jump()
                    
            if event.key == pygame.K_f:
                if player.attacking == False:
                    player.attacking = True
                    player.attack()

    if player.health <= 0:
        pass

    player.move()
    player.touching_ground()
    player.run_animation()
    if player.attacking:
        player.attack()

    player.enemy_collision()
  
    enemy_generation()
    background.render(display_surface)
    ground.render(display_surface)
    Health.render(display_surface)

    for entity in all_characters:
        display_surface.blit(entity.image, entity.rect)

    for entity in enemy_group:
        entity.move()
        if entity.health <= 0:
            entity.kill()
            dead_group.add(entity)
            
            death_message_cond = True
            pygame.time.set_timer(death_message_timer, 2000)
            ENEMY_KILLED_X = entity.rect.centerx
            ENEMY_KILLED_Y = entity.rect.centery
            display_surface.blit(enemy_killed_msg, (ENEMY_KILLED_X, ENEMY_KILLED_Y))

    if death_message_cond:
        display_surface.blit(enemy_killed_msg, (ENEMY_KILLED_X, ENEMY_KILLED_Y))

    pygame.display.update() 
    FPS_CLOCK.tick(FPS)

