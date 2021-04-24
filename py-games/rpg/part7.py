# collision detection 1
import pygame
from pygame.locals import *
import sys
import random

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


pygame.init()  # Begin pygame
vec = pygame.math.Vector2

# CLASS INTERFACES
HEIGHT = 550
WIDTH = 1000
ACC = 0.5
FRIC = -0.1
JUMP = -7
GRAVITY = 0.25
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

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
        self.surf = pygame.Surface((WIDTH, 20))
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
        self.direction = "RIGHT"

        # movement 
        self.jumping = False
        self.running = False
        self.move_frame = 0

        # attack
        self.attacking = False
        self.attack_frame = 0
        self.cooldown = False

    def gravity_check(self):
      hits = pygame.sprite.spritecollide(player ,ground_group, False)
      if self.vel.y > 0:
          if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.jumping = False
              #lowest = hits[0]
              #if self.pos.y <= lowest.rect.bottom:
                  #self.pos.y = lowest.rect.top + 1
                  #self.vel.y = 0
                  #self.jumping = False

    def move(self):
        self.acc = vec(0, GRAVITY)
        
        # Set running to False when player slows down 
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC 
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  

        # Wrap player around screen width
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
       
        self.rect.midbottom = self.pos  # Update rect with new pos   


    def update(self):
        # Return to base frame if at end of movement sequence 
        if self.move_frame >= 9:
            self.move_frame = 0
            return

        # Update to next frame
        if self.jumping == False and self.running == True:  
            if self.vel.x > 0:
                self.image = run_R[self.move_frame]
                self.direction = "RIGHT"
            elif self.vel.x < 0:
                self.image = run_L[self.move_frame]
                self.direction = "LEFT"
            self.move_frame += 1
        
        # Returns to base frame if standing still and incorrect frame is showing
        if abs(self.vel.x) < 0.2 and self.move_frame != 0:
            self.move_frame = 0
            if self.direction == "RIGHT":
                self.image = run_R[self.move_frame]
            elif self.direction == "LEFT":
                self.image = run_L[self.move_frame]
    
    def attack(self):        
        # If end of sequence, return to base frame      
        if self.attack_frame >= 9:
            self.attack_frame = 0
            self.attacking = False
 
        # Check direction for correct animation to display  
        if self.direction == "RIGHT":
            self.image = attack_R[self.attack_frame]
        elif self.direction == "LEFT":
            self.image = attack_L[self.attack_frame]  
        self.attack_frame += 1
    
    def jump(self):
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = JUMP
            
    def gets_hit(self):
        if self.cooldown == False:      
            self.cooldown = True # Enable the cooldown
            pygame.time.set_timer(hit_cooldown, 1000) # Resets cooldown in 1 second
            
        print("hit")
        pygame.display.update()

    def render(self):
        display_surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/Enemy.png")
        self.rect = self.image.get_rect()     
        self.pos = vec(0,0)
        self.vel = vec(0,0)
        self.direction = random.randint(0,1) # 0 for Right, 1 for Left
        self.vel.x = random.randint(2,6) / 2  # Randomized velocity of the generated enemy
        self.alive = True
        # Sets the intial position of the enemy
        if self.direction == 0:
            self.pos.x = 0
            self.pos.y = HEIGHT-150
        if self.direction == 1:
            self.pos.x = 700
            self.pos.y = HEIGHT-150

    def move(self):
        # At the edges of screen, change direction   
        if self.pos.x >= (WIDTH-20):
                self.direction = 1
        elif self.pos.x <= 0:
                self.direction = 0
        # Updates position with new values     
        if self.direction == 0:
            self.pos.x += self.vel.x
        if self.direction == 1:
            self.pos.x -= self.vel.x
        self.rect.center = self.pos # Updates rect

    def update(self):
        # Check for collision with Player
        hits = pygame.sprite.spritecollide(self, Playergroup, False)
 
        # If player is attack, call "kill" method
        if hits and player.attacking == True:
            self.kill()
            print("Enemy killed")
            self.alive = False
        
        # If player not attacking, call "hit" function            
        elif hits and player.attacking == False:
            hits[0].gets_hit()
    
  
    def render(self):
        if self.alive:
            display_surface.blit(self.image, (self.pos.x, self.pos.y))


# ---- GAME SETUP ----- #
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# BACKGROUND OBJECTS
background = Background()
ground = Ground()
ground_group = pygame.sprite.Group()
ground_group.add(ground)

# CHARACTER OBJECTS
player = Player()
enemy = Enemy()
Playergroup = pygame.sprite.Group()
Playergroup.add(player)

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
                    player.jump()
            if event.key == pygame.K_RETURN:
                if player.attacking == False:
                    player.attack()
                    player.attacking = True  

        if event.type == hit_cooldown:
            player.cooldown = False
            pygame.time.set_timer(hit_cooldown, 0)

    # Updating player
    player.move()
    enemy.move()
    player.update()
    if player.attacking == True:
        player.attack() 
    
    enemy.update()
    player.gravity_check()

    # Updating objects on main display
    background.render(display_surface)
    ground.render(display_surface)
    player.render()
    enemy.render()

    # Updating main display
    pygame.display.update() 
    FPS_CLOCK.tick(FPS)
