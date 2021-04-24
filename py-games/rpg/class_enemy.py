import pygame
from pygame.locals import *
import random

HEIGHT = 600
WIDTH = 800
ACC = 0.5
FRIC = -0.1
JUMP = -7
GRAVITY = 0.25
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
vec = pygame.math.Vector2

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

    def update(self, player, player_group, hit_cooldown):
        # Check for collision with Player
        hits = pygame.sprite.spritecollide(self, player_group, False)
 
        # If player is attack, call "kill" method
        if hits and player.attacking == True:
            self.kill()
            self.alive = False
            if player.mana < 100: player.mana += self.mana # Release mana
            player.experiance += 1   # Release expeiriance
            
            rand_num = numpy.random.uniform(0, 100)
            item_no = 0
            if rand_num >= 0 and rand_num <= 5:  # 1 / 20 chance for an item (health) drop
                    item_no = 1
            elif rand_num > 5 and rand_num <= 15:
                    item_no = 2
            if item_no != 2:
                # Add Item to Items group
                item = Item(item_no)
                Items.add(item)
                # Sets the item location to the location of the killed enemy
                item.posx = self.pos.x
                item.posy = self.pos.y
        
        # If player not attacking, call "hit" function            
        elif hits and player.attacking == False:
            hits[0].gets_hit(hit_cooldown)
    
  
    def render(self, display_surface):
        if self.alive:
            display_surface.blit(self.image, (self.pos.x, self.pos.y))

