import pygame
import random

# you need monocraft font for this game

pygame.init()

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Sun Quest ')
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
ORANGE = (255, 165, 0)
RED = (220, 20, 60)

# grid
GRIDSIZE = 20

# resetting game
def reset_game():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (0, 0)
    score = 0
    food_x = (random.randint(0, (WIDTH - GRIDSIZE) // GRIDSIZE) * GRIDSIZE)
    food_y = (random.randint(0, (HEIGHT - GRIDSIZE) // GRIDSIZE) * GRIDSIZE)
    food = food_x, food_y
    game_over = False
    game_run = True

    return snake, direction, score, food, game_over, game_run

snake, direction, score, food, game_over, game_run = reset_game()
# sun
sun_r = 50
sun_color = 0
sun_rise = 0


# start screen
snake_font = pygame.font.Font(monocraft, 60)
snake_text = snake_font.render('Sun Quest III', True, YELLOW)
snake_text_rect = snake_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 50))
snake2_font = pygame.font.Font(monocraft, 40)
snake2_text = snake2_font.render('Free The Sun', True, YELLOW)
snake2_text_rect = snake2_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))

start_font = pygame.font.Font(monocraft, 30)
start_text = start_font.render('Press SPACE to begin', True, YELLOW)
start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))

info_font = pygame.font.Font(monocraft, 15)
info_text = info_font.render('Collect 20 sun particles to free the sun', True, YELLOW)
info_text_rect = info_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 120))
# game over
game_over_font = pygame.font.Font(monocraft, 24)
game_over_text = game_over_font.render('Game Over', True, YELLOW)
game_over_text_rect = game_over_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 50))

restart_text_font = pygame.font.Font(monocraft, 20)
restart_text = game_over_font.render('Press R to restart', True, YELLOW)
restart_text_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 90))

# beat game
end_font = pygame.font.Font(monocraft, 24)
end_text = end_font.render('You saved the sun!', True, BLACK)
end_text_rect = end_text.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 50))


ready = True
end = False

# ---------------------------

running = True
while running:
    # EVENT HANDLING

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if ready:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ready = False
                game_run = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # restart game
                snake, direction, score, food, game_over, game_run = reset_game()

    # updating score
    score_text = game_over_font.render(f'Score: {score}', True, RED)
    score_text_rect = score_text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
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

    # background before start
    if ready:
        screen.fill((0, 0, 50))
        for pos in stars:
            pygame.draw.ellipse(screen, (255, 255, 255), (pos[0], pos[1], 5, 5))
        screen.blit(start_text, start_text_rect)
        screen.blit(info_text, info_text_rect)
        screen.blit(snake_text, snake_text_rect)
        screen.blit(snake2_text, snake2_text_rect)
        pygame.display.flip()

    # after start
    elif game_run:
        # snake body
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, head)
        # collision
        if head == food:
            score += 1
            print(f'Your current score is {score}.')
            food_check = True
            # spawn food again
            while food_check:
                food_x = (random.randint(0, (WIDTH - GRIDSIZE) // GRIDSIZE) *
                        GRIDSIZE)
                food_y = (random.randint(0, (HEIGHT - GRIDSIZE) // GRIDSIZE) *
                        GRIDSIZE)
                food = food_x, food_y
                
                for j in range(len(snake)):
                    if food not in snake:
                        food_check = False

            if score == 20: # change this to 1 to go straight to end
                end = True
                game_run = False
        else:
            snake.pop()
        # self collision
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            game_over = True
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
        pygame.draw.rect(screen, YELLOW, (*food, GRIDSIZE, GRIDSIZE))
        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRIDSIZE, GRIDSIZE))

    # game over
    elif game_over:
        screen.fill(BLACK)
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(restart_text, restart_text_rect)

    # game beat
    elif end:
        screen.fill((sun_color, sun_color, 0))
        if sun_color <= 190:
            for pos in stars:
                pygame.draw.ellipse(screen, (255, 255, 255), (pos[0], pos[1], 5, 5))
        screen.blit(end_text, end_text_rect)
        screen.blit(score_text, score_text_rect)
        pygame.draw.circle(screen, (255, 255, 0), (WIDTH // 2, HEIGHT + sun_r - sun_rise), sun_r)
        pygame.draw.circle(screen, ORANGE, (WIDTH // 2, HEIGHT + sun_r - sun_rise), sun_r - 10)
        if sun_color != 200:
            sun_color += 2
        if sun_rise != 260:
            sun_rise += 2


    pygame.display.flip()
    clock.tick(10)
    #---------------------------


pygame.quit()
