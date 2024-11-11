# Reach The Sun

import random
import pygame
from pygame.locals import K_ESCAPE, QUIT, K_RIGHT, K_LEFT

# Initialize Pygame
pygame.init()

# Import Keys
from pygame.locals import K_ESCAPE, K_SPACE, KEYDOWN, QUIT, K_RIGHT, K_LEFT

# Set Display
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Reach The Sun")

current_screen = 0
running = True

# Colour Variables
black = (0, 0, 0)
black2 = (50, 50, 50)
white = (255, 255, 255)
yellow = (228, 208, 10)
blue = (0, 71, 171)
blue2 = (0, 60, 190)
orange = (255, 172, 28)
red = (255, 35, 35)

# User Variables
user_x = WIDTH/2
user_y = HEIGHT - 200
user_speed = 1

# Game Variables
game_width = 600 
stars = []
for s in range(100):
    star_x = random.randrange(0, WIDTH)
    star_y = random.randrange(0, HEIGHT)
    star_pos = (star_x, star_y)
    stars.append(star_pos)
    
current_screen = 0
running = True
monocraft = 'Monocraft.ttf'

obstacles = []
obstacle_speed = 0.5
previous_obstacle_y = -100

for o in range(5):
    obstacle_x = random.randint(200, 200 + game_width)  # Keep obstacles within game area
    obstacle_y = random.randint(-100, -10)  # Start slightly off-screen
    obstacle_width = random.randint(100, 150)
    obstacle_height = 50
    obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    previous_obstacle_y = obstacle_y

# Title Text
title_font = pygame.font.Font(monocraft, 75)
title = title_font.render("REACH THE SUN", True, (orange))
title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
# Start Text
start_font = pygame.font.Font(monocraft, 50)
start = start_font.render("Press Space to Start", True, (white))
start_rect = start.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
# Description Text
desc_font = pygame.font.Font(monocraft, 22)
desc = desc_font.render("Use the Left and Right Arrow Keys to Dodge Incoming Obstacles", True, (orange))
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
        screen.fill(blue)
        # Import text
        screen.blit(title, title_rect)
        screen.blit(start, start_rect)        
        # Draw Stars
        for star_x, star_y in stars:
            pygame.draw.circle(screen, white, (star_x, star_y), 2)
            
    # Countdown Screen
    elif current_screen == 1:
        screen.fill(blue2)
        count_font = pygame.font.Font(monocraft, 125)
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
        screen.fill(black)
        pygame.draw.rect(screen, black2, (200, 0, game_width, HEIGHT))
        pygame.draw.circle(screen, blue2, (user_x, user_y), 50)
        # Draw Stars
        for star_x, star_y in stars:
            pygame.draw.circle(screen, white, (star_x, star_y), 2)
        # Get state of all keys
        keys = pygame.key.get_pressed()
        # User movement
        if keys[K_RIGHT] and user_x + 50 + user_speed < game_width + 200:
            user_x += user_speed
        if keys[K_LEFT] and user_x - 50 - user_speed > 200:
            user_x -= user_speed
                    # Move and draw obstacles
        active_obstacles = 0  # Track active obstacles at same y level
        for obstacle in obstacles:
        # Move obstacle down if it is within screen bounds
            if obstacle[1] <= HEIGHT:
                obstacle[1] += obstacle_speed
                active_obstacles += 1
                pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))
            
        # Reset obstacle if it reaches the bottom
            if obstacle[1] > HEIGHT:
                # Only reset if less than 2 obstacles are active at the same level
                if active_obstacles < 2:
                    obstacle[0] = random.randint(200, 200 + game_width)  # New random x position
                    obstacle[1] = - random.randint(100, 200)  # Position above the screen
                    active_obstacles += 1

    pygame.display.flip()
