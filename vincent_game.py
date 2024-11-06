import pygame
import random


pygame.init()

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# grid
GRIDSIZE = 20

# snake
SNKWIDTH = 20
SNKHEIGHT = 20

snake_body = []

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    screen.fill(BLACK)  # always the first drawing command
    for i in range(0, WIDTH, GRIDSIZE * 2):
        for j in range(0, HEIGHT, GRIDSIZE * 2):
            pygame.draw.rect(screen, WHITE, (i, j, GRIDSIZE, GRIDSIZE))
    for i in range(GRIDSIZE, WIDTH, GRIDSIZE * 2):
        for j in range(GRIDSIZE, HEIGHT, GRIDSIZE * 2):
            pygame.draw.rect(screen, WHITE, (i, j, GRIDSIZE, GRIDSIZE))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
