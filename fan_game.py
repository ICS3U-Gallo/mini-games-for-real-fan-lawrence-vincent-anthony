# Avoid The Obstacles

import random
import pygame
from pygame.locals import K_ESCAPE, QUIT, K_RIGHT, K_LEFT

pygame.init()

# Set Display
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Avoid the Obstacles by Fan")

current_screen = 0
running = True

# Colour Variables
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.key == K_ESCAPE:
            running = False
    if current_screen == 0:
        screen.fill(black)
