# Reach The Sun

import random
import pygame
from pygame.locals import K_ESCAPE, QUIT, K_RIGHT, K_LEFT

# Initialize Pygame
pygame.init()

# Import Keys
from pygame.locals import K_ESCAPE, K_SPACE, KEYDOWN, QUIT, K_RIGHT, K_LEFT

# Set Display
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Reach The Sun")

current_screen = 0
running = True

# Colour Variables
black = (0, 0, 0)
black2 = (50, 50, 50)
white = (255, 255, 255)
gray = (128, 128, 128)

current_screen = 0
running = True
monocraft = 'Monocraft.ttf'

# Title Text
title_font = pygame.font.Font(monocraft, 75)
title = title_font.render("REACH THE SUN", True, (white))
title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
# Start Text
start_font = pygame.font.Font(monocraft, 50)
start = start_font.render("Press Space to Start", True, (white))
start_rect = start.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
# Desc Text
desc_font = pygame.font.Font(monocraft, 22)
desc = desc_font.render("Use the Left and Right Arrow Keys to Dodge Incoming Obstacles", True, (white))
desc_rect = desc.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))

# ------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:  
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE:
                current_screen += 1
                
    # Start Screen
    if current_screen == 0:
        screen.fill(black)
        screen.blit(title, title_rect)
        screen.blit(start, start_rect)
        
    # Countdown Screen
    elif current_screen == 1:
        screen.fill(gray)
        count_font = pygame.font.Font(monocraft, 75)
        for i in range(5, 0, -1):
            screen.fill(gray)
            screen.blit(desc, desc_rect)
            count = count_font.render(f"{i}", True, (white))  
            count_rect = count.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(count, count_rect)
            pygame.display.flip()
            pygame.time.wait(1000)
        current_screen += 1
    elif current_screen == 2:
        screen.fill(black2)
        

    pygame.display.flip()
