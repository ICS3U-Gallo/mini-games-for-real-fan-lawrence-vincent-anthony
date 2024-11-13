# Reach The Sun

import random
import pygame

# Intialize pygame
pygame.init()

# Import Keys
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_RIGHT, K_LEFT

# Set Display
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reach The Sun")

# Colour Variables
black = (0, 0, 0)
black2 = (20, 20, 20)
white = (255, 255, 255)
yellow = (228, 208, 10)
blue = (0, 71, 171)
blue2 = (0, 60, 190)
orange = (255, 172, 28)
red = (255, 35, 35)

# User Variables
user_x = WIDTH / 2
user_y = HEIGHT - 200
user_speed = 1.5

# Game Variables
stars = []
for s in range(100):
    star_x = random.randint(0, WIDTH)
    star_y = random.randint(0, HEIGHT)
    star_pos = (star_x, star_y)
    stars.append(star_pos)

current_screen = 0
running = True
monocraft = 'Monocraft.ttf'
game_over = False

# Obstacle variables
obstacle_speed = 0.5
obstacles = []
previous_obstacle_y = -100

for o in range(5):
    obstacle_x = random.randint(0, WIDTH)  # Keep obstacles within game area
    obstacle_y = previous_obstacle_y - random.randint(100, 150)  # Start slightly off-screen
    obstacle_width = 100
    obstacle_height = 50
    obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    previous_obstacle_y = obstacle_y


# Title Text
title_font = pygame.font.Font(monocraft, 100)
title = title_font.render("SUN QUEST II", True, (orange))
title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Subtitle Text
subtitle_font = pygame.font.Font(monocraft, 75)
subtitle = subtitle_font.render("REACH THE SUN", True, (orange))
subtitle_rect = subtitle.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
# Start Text
start_font = pygame.font.Font(monocraft, 50)
start = start_font.render("Start", True, (white))
start_rect = start.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
start_button = pygame.Rect(WIDTH/2 - 150, HEIGHT/2 + 80, 300, 60)
# Instructions Text
instructions_font = pygame.font.Font(monocraft, 50)
instructions = instructions_font.render("Instructions", True, (white))
instructions_rect = instructions.get_rect(center=(WIDTH/2, HEIGHT/2 + 250))
instructions_button = pygame.Rect(WIDTH/2 - 150, HEIGHT/2 + 180, 300, 60)
# Description Text
desc_font = pygame.font.Font(monocraft, 22)
desc = desc_font.render("Use the Left and Right Arrow Keys to Dodge Incoming Obstacles", True, (orange))
desc_rect = desc.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Game Over Text
game_over_font = pygame.font.Font(monocraft, 75)
game_over_text = game_over_font.render("GAME OVER", True, red)
game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))

button_default_color = blue2
button_hover_color = blue

# -------------------------------------

while running:
    # Update mouse position every frame
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                current_screen -= 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if user clicked Start
            if current_screen == 0 and start_button.collidepoint(mouse_x, mouse_y):
                current_screen = 2  # Move to the game screen
            # Check if user clicked Instructions
            elif current_screen == 0 and instructions_button.collidepoint(mouse_x, mouse_y):
                current_screen = 1  # Move to the instructions screen 

    # Start Screen
    if current_screen == 0:
        screen.fill(blue)
        # Draw buttons with hover effect
        pygame.draw.rect(screen, button_hover_color if start_button.collidepoint(mouse_x, mouse_y) else button_default_color, start_button)
        pygame.draw.rect(screen, button_hover_color if instructions_button.collidepoint(mouse_x, mouse_y) else button_default_color, instructions_button)
        # Import text
        screen.blit(title, title_rect)
        screen.blit(subtitle, subtitle_rect)
        screen.blit(start, start_rect)
        screen.blit(instructions, instructions_rect)
        # Draw Stars
        for star_x, star_y in stars:
            pygame.draw.circle(screen, white, (star_x, star_y), 2)

    # Instructions Screen
    elif current_screen == 1:
        screen.fill(blue2)
        screen.blit(desc, desc_rect)
        back_text = instructions_font.render("Press ESC to go back", True, white)
        back_text_rect = back_text.get_rect(center=(WIDTH / 2, HEIGHT - 100))
        screen.blit(back_text, back_text_rect)
    
    # Game Screen
    elif current_screen == 2:
        screen.fill(black)
        pygame.draw.circle(screen, blue2, (user_x, user_y), 40) # Draw player
        # Draw Stars
        for star_x, star_y in stars:
            pygame.draw.circle(screen, white, (star_x, star_y), 2)
        # Get state of all keys
        keys = pygame.key.get_pressed()
        # User movement
        if keys[K_RIGHT] and user_x + 40 + user_speed <= WIDTH:
            user_x += user_speed
        if keys[K_LEFT] and user_x - 40 - user_speed >= 0:
            user_x -= user_speed
        # Move and draw obstacles
        active_obstacles = 0  # Track active obstacles at same y level
        for obstacle in obstacles:
            # Move obstacle down if it is within screen bounds
            if obstacle[1] <= HEIGHT:
                obstacle[1] += obstacle_speed
                active_obstacles += 1
                pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))

                # Calculate the closest point on the obstacle to the center of the player
                closest_x = max(obstacle[0], min(user_x, obstacle[0] + obstacle[2]))
                closest_y = max(obstacle[1], min(user_y, obstacle[1] + obstacle[3]))

                # Calculate the distance from the player center to this closest point
                distance_x = user_x - closest_x
                distance_y = user_y - closest_y
                distance = (distance_x**2 + distance_y**2) ** 0.5

                # Check if the distance is less than the player's radius
                if distance < 40:
                    game_over = True
            # Reset obstacle if it reaches the bottom
            if obstacle[1] > HEIGHT:
                # Randomize new x-position within the game area and place it above the screen
                obstacle[0] = random.randint(0, WIDTH - obstacle[2])
                obstacle[1] = random.randint(-150, -100)  # Place it at a random height above the screen
    # Game over
    if game_over:
        pygame.time.wait(1000) # Freeze game 1 second after losing
        screen.fill(black)
        screen.blit(game_over_text, game_over_rect)
        pygame.display.flip()


    pygame.display.flip()

