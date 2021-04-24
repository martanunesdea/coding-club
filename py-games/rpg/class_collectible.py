import pygame
from pygame.locals import *

class Item(pygame.sprite.Sprite):
    def __init__(self, itemtype):
        super().__init__()
        if itemtype == 1: 
            self.image = pygame.image.load("assets/health_one.png")
        elif itemtype == 2: 
            self.image = pygame.image.load("coin.png")
        
        self.rect = self.image.get_rect()
        self.type = itemtype
        self.posx = 0
        self.posy = 0

    def render(self, display_surface):
        self.rect.x = self.posx
        self.rect.y = self.posy
        display_surface.blit(self.image, self.rect)
    
    def update(self, player, player_group, health_bar):
        hits = pygame.sprite.spritecollide(self, player_group, False)
        # Code to be activated if item comes in contact with player
        if hits:
            if player.health < 5 and self.type == 1:
                player.health += 1
                self.kill()
            if self.type == 2:
                player.exp += 1
                self.kill()