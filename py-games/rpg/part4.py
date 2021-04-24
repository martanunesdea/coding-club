# animations
import pygame
from pygame.locals import *
import sys
import random

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

# CONSTANTS
HEIGHT = 550
WIDTH = 1000
ACC = 0.5
FRIC = -0.1
JUMP = -7
GRAVITY = 0.25
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0

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
        self.jumping = False
        self.direction = "RIGHT"
        self.running = False
        self.move_frame = 0

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
        
        # Set running to False if the player has slowed down to a certain extent
        if abs(self.vel.x) > 0.3:
            self.running = True
        else:
            self.running = False

        # Returns the current key presses
        pressed_keys = pygame.key.get_pressed()
        # Accelerates the player in the direction of the key press
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC 
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # Updates Position with new values

        # This causes character wrapping from one point of the screen to the other
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
        # Move the character to the next frame if conditions are met 
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
        pass
    
    def jump(self):
        # Check to see if payer is in contact with the ground
        hits = pygame.sprite.spritecollide(self, ground_group, False)
        # If touching the ground, and not currently jumping, cause the player to jump.
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = JUMP
     
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()


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

    # Updating player
    player.move()
    player.update()
    player.gravity_check()
    
    # Updating objects on main display
    background.render(display_surface)
    ground.render(display_surface)
    display_surface.blit(player.image, player.rect)

    # Updating main display
    pygame.display.update() 
    FPS_CLOCK.tick(FPS)
