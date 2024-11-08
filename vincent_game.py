import pygame
import random


pygame.init()

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('sun collector')
monocraft = 'Monocraft.ttf'

# ---------------------------
# Initialize global variables

# start screen
stars = []
for i in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pos = x, y
        stars.append(pos)

# colors
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)

# grid
GRIDSIZE = 20

# snake
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (0, 0)

food_x = (random.randint(0, (WIDTH - GRIDSIZE) // GRIDSIZE) * GRIDSIZE) 
food_y = (random.randint(0, (HEIGHT - GRIDSIZE) // GRIDSIZE) * GRIDSIZE)
food = food_x, food_y
score = 0

# start screen
snake_font = pygame.font.Font(monocraft, 75)
snake_text = snake_font.render('SUN EATER', True, YELLOW)
snake_text_rect = snake_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

start_font = pygame.font.Font(monocraft, 30)
start_text = start_font.render('Press SPACE to begin', True, YELLOW)
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))

info_font = pygame.font.Font(monocraft, 15)
info_text = info_font.render('Use arrow keys to control the snake', True, YELLOW)
info_text_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))

ready = True
game_run = False
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ready = False
            game_run = True
    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction[1] == 0:
        direction = (0, -GRIDSIZE)
    elif keys[pygame.K_DOWN] and direction[1] == 0:
        direction = (0, GRIDSIZE)
    elif keys[pygame.K_LEFT] and direction[0] == 0:
        direction = (-GRIDSIZE, 0)
    elif keys[pygame.K_RIGHT] and direction[0] == 0:
        direction = (GRIDSIZE, 0)
    # GAME STATE UPDATES
    # All game math and comparisons happen here

    # DRAWING
    if ready:
        screen.fill((0, 0, 50))  # always the first drawing command
        for pos in stars:
            pygame.draw.rect(screen, (255, 255, 255), (pos[0], pos[1], 5, 5))
        screen.blit(start_text, start_text_rect)
        screen.blit(info_text, info_text_rect)
        screen.blit(snake_text, snake_text_rect)
        pygame.display.flip()

    elif game_run:
        # snake body
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)
        # collision
        if head == food:
            score += 1
            print(f'Your current score is {score}.')
            food_x = (random.randint(0, (WIDTH - GRIDSIZE) // GRIDSIZE) *
                    GRIDSIZE)
            food_y = (random.randint(0, (HEIGHT - GRIDSIZE) // GRIDSIZE) *
                    GRIDSIZE)
            food = food_x, food_y
        else:
            snake.pop()
        # self collision
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            game_run = False
        # grid
        screen.fill(BLACK)  
        for i in range(0, WIDTH, GRIDSIZE * 2):
            for j in range(0, HEIGHT, GRIDSIZE * 2):
                pygame.draw.rect(screen, GRAY, (i, j, GRIDSIZE, GRIDSIZE))
        for i in range(GRIDSIZE, WIDTH, GRIDSIZE * 2):
            for j in range(GRIDSIZE, HEIGHT, GRIDSIZE * 2):
                pygame.draw.rect(screen, GRAY, (i, j, GRIDSIZE, GRIDSIZE))
        # Draw food
        pygame.draw.rect(screen, YELLOW, (food_x, food_y, GRIDSIZE, GRIDSIZE))
        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, GRIDSIZE, GRIDSIZE))
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(10)
    #---------------------------


pygame.quit()
