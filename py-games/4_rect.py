import pygame
from pygame.locals import *
import sys

rect1 = pygame.Rect((20, 50), (50, 100))

""" Attributes """
print("Rect 1 coordinates: ", rect1.x, ", ", rect1.y)
print("Rect 1 top: ", rect1.top)
print("Rect 1 bottom: ", rect1.bottom)
print("Rect 1 left: ", rect1.left)
print("Rect 1 right: ", rect1.right)
print("Rect 1 center: ", rect1.center)
print("Rect 1 center in X-dimension: ", rect1.centerx)
print("Rect 1 center in Y-dimension: ", rect1.centery)


""" Rect.move and Rect.move_ip 
# Rect move will create a new rect, in a different place
rect2 = rect1.move(100, 100)
print("Position of moved rect1: ", rect2.topleft)
print("Position of rect1: ", rect1.topleft)
print("\n\n")
# Rect move_ip will replace the previous coordinates
rect1.move_ip(100, 100)
print("Position of rect1: rect1.topleft)
"""

"""  Experiment to convince further: move_ip doesn't return anything..
rect3 = rect1.move_ip(100, 100)
print("Position of moved rect1: ", rect5.topleft)
print("Position of rect1: ", rect1.topleft)
"""



""" Collision
rect3 = pygame.Rect((10, 10), (100, 100))
rect4 = pygame.Rect((0, 0), (50, 50))
 
if rect1.colliderect(rect3):
    print("rect 1 and rect 3 clash")
if rect1.colliderect(rect4):
    print("rect 1 and rect 4 clash")
if rect3.colliderect(rect4):
    print("rect 3 and rect 4 clash")
"""