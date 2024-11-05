# pygame ball brick breaker game 

import pygame
import random


pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables  
BALL_RADIUS = 8
ball_speed_x = 4 
ball_speed_y = -4
paddle_width = 80
paddle_length = 10  
brick_width = 60
brick_height = 20
brick = []

stars = []
for _ in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    pos = (x, y)
    stars.append(pos)


# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)

    # GAME STATE UPDATES
    # All game math and comparisons happen here




    # DRAWING
    screen.fill((0,0,0))  # always the first drawing command
    pygame.draw.rect(screen,(225,225,225), (WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_length))
    pygame.draw.ellipse(screen,(225,0,0),(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2))

    for x, y in stars:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))

    for i in range(8):
        pygame.draw.rect((screen),(225,0,0)

    



    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
