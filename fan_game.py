# Reach The Sun

import random
import pygame

# Intialize pygame
pygame.init()

# Import Keys
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_RIGHT, K_LEFT, K_r

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
orange2 = (195, 150, 15)
red = (255, 35, 35)

# User Variables
user_x = WIDTH / 2
user_y = HEIGHT - 200
user_speed = 1.5

# Game Variables
stars = []
for s in range(125):
    star_x = random.randint(0, WIDTH)
    star_y = random.randint(0, HEIGHT)
    star_pos = (star_x, star_y)
    stars.append(star_pos)

current_screen = 0
running = True
monocraft = 'Monocraft.ttf'
sun_y = -200
game_won_num = 150 # Amount of obstacles dodged needed to win
obstacles_dodged = 0
timer = 0

# Obstacle variables
obstacle_speed = 0.5
last_speed_increase = pygame.time.get_ticks()
obstacles = []
previous_obstacle_y = -100
for o in range(5):
    obstacle_x = random.randint(0, WIDTH-150)  # Keep obstacles within game area
    obstacle_y = previous_obstacle_y - random.randint(100, 150)  # Start slightly off-screen
    obstacle_width = 150
    obstacle_height = 50
    obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    previous_obstacle_y = obstacle_y


try:
    monocraft_font = 'Monocraft.ttf' # Attempt to use Monocraft font
    intro_font = pygame.font.Font(monocraft, 28)
    title_font = pygame.font.Font(monocraft_font, 100)  
    subtitle_font = pygame.font.Font(monocraft_font, 75)
    start_font = pygame.font.Font(monocraft_font, 50)
    desc_font = pygame.font.Font(monocraft_font, 30)
    back_font = pygame.font.Font(monocraft_font, 30)
    game_over_font = pygame.font.Font(monocraft_font, 75)
    restart_font = pygame.font.Font(monocraft_font, 50)
    win_font = pygame.font.Font(monocraft, 60)
except FileNotFoundError:
    intro_font = pygame.font.Font('arial', 28)
    title_font = pygame.font.SysFont('arial', 100)  # Use Arial if Monocraft is not in system
    subtitle_font = pygame.font.SysFont('arial', 75)
    start_font = pygame.font.SysFont('arial', 50)
    desc_font = pygame.font.SysFont('arial', 30)
    back_font = pygame.font.SysFont('arial', 30)
    game_over_font = pygame.font.SysFont('arial', 75)
    restart_font = pygame.font.SysFont('arial', 50)
    win_font = pygame.font.SysFont('arial', 60)

# Intro Text
intro = intro_font.render("The sun has disappeared...", True, (white))
intro_rect = intro.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Intro Desc 
intro_desc = intro_font.render("You must reach it to restore light in the world...", True, (white))
intro_desc_rect = intro_desc.get_rect(center=(WIDTH/2, HEIGHT/2))
# Title Text
title = title_font.render("SUN QUEST II", True, (orange))
title_rect = title.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Subtitle Text
subtitle = subtitle_font.render("REACH THE SUN", True, (orange))
subtitle_rect = subtitle.get_rect(center=(WIDTH/2, HEIGHT/2 - 100))
# Start Text
start = start_font.render("Start", True, (white))
start_rect = start.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
start_button = pygame.Rect(WIDTH/2 - 150, HEIGHT/2 + 70, 300, 70)
# Instructions Text
instructions = start_font.render("Instructions", True, (white))
instructions_rect = instructions.get_rect(center=(WIDTH/2, HEIGHT/2 + 250))
instructions_button = pygame.Rect(WIDTH/2 - 250, HEIGHT/2 + 215, 500, 70)
# Description Text
desc = desc_font.render("Use the Left and Right Arrow Keys to Move", True, (orange))
desc_rect = desc.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Go Back Text
back_text = back_font.render("Press ESC to go back", True, white)
back_text_rect = back_text.get_rect(center=(WIDTH / 2, HEIGHT - 200))
# Game Over Text
game_over_text = game_over_font.render("GAME OVER", True, red)
game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2 - 200))
# Restart Game Text
restart_text = restart_font.render("Press R to Restart", True, yellow)
restart_rect = restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 100))
# Game Won Text
win_text = win_font.render("SUN QUEST II: COMPLETE!", True, yellow)
win_rect = win_text.get_rect(center=(WIDTH/2, 300))

game_over = False

button_default_color = orange2
button_hover_color = orange

# -------------------------------------

while running:
    # Update mouse position every frame
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and (game_over or current_screen == 5):
                # Reset all game variables
                user_x = WIDTH/2
                user_speed = 1.5
                sun_y = -200
                obstacle_speed = 0.5
                obstacles_dodged = 0
                last_speed_increase = pygame.time.get_ticks()
                current_screen = 3  # Go back to the start game screen
                game_over = False

                # Reinitialize stars
                stars = []
                for s in range(125):
                    star_x = random.randint(0, WIDTH)
                    star_y = random.randint(0, HEIGHT)
                    stars.append((star_x, star_y))

                # Reinitialize obstacles
                obstacles = []
                previous_obstacle_y = -100
                for o in range(5):
                    obstacle_x = random.randint(0, WIDTH - 150)
                    obstacle_y = previous_obstacle_y - random.randint(100, 150)
                    obstacle_width = 150
                    obstacle_height = 50
                    obstacles.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])
                    previous_obstacle_y = obstacle_y

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Check if user clicked Start
            if current_screen == 1 and start_button.collidepoint(mouse_x, mouse_y):
                current_screen = 3  # Move to the game screen
                start_time = pygame.time.get_ticks()
            # Check if user clicked Instructions
            elif current_screen == 1 and instructions_button.collidepoint(mouse_x, mouse_y):
                current_screen = 2  # Move to the instructions screen 
                
    # Intro Screen
    if current_screen == 0:
        fade_surface = pygame.Surface((WIDTH, HEIGHT))  # Create a surface for the fade effect
        fade_surface.fill(black)
        fade_surface.set_alpha(255)  # Start fully opaque
        
        fade_alpha = 255  # Transparency value
        
        while fade_alpha > 0:
            screen.fill(black)
            screen.blit(intro, intro_rect)
            screen.blit(intro_desc, intro_desc_rect)
            
            # Gradually reduce the alpha value for fade-in
            fade_alpha -= 5
            if fade_alpha < 0:
                fade_alpha = 0  # Ensure it doesn't go below 0
            
            fade_surface.set_alpha(fade_alpha)
            screen.blit(fade_surface, (0, 0))
            
            pygame.display.flip()
            pygame.time.delay(75)  # Control speed of fading

        # Move to start screen
        current_screen = 1

    # Start Screen
    if current_screen == 1:
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
    elif current_screen == 2:
        screen.fill(blue2)
        screen.blit(desc, desc_rect)
        screen.blit(back_text, back_text_rect)
        for event in pygame.event.get():
            if event.type == KEYDOWN: 
                if event.key == K_ESCAPE:
                    current_screen = 1
    
    # Game Screen
    elif current_screen == 3:
        # Fill the screen
        screen.fill(black)

        # Update timer for debugging or time tracking
        timer = pygame.time.get_ticks() - start_time

        # Draw the sun
        pygame.draw.circle(screen, red, (WIDTH // 2, int(sun_y)), 120)
        pygame.draw.circle(screen, orange, (WIDTH // 2, int(sun_y)), 100)

        # Draw the player
        pygame.draw.circle(screen, white, (int(user_x), int(user_y)), 40)
        pygame.draw.circle(screen, blue2, (int(user_x), int(user_y)), 30)

        # Move and draw stars
        for i in range(len(stars)):
            star_x, star_y = stars[i]
            star_y += obstacle_speed  # Move stars downward
            if star_y > HEIGHT:  # Reset stars when they move off the screen
                star_x = random.randint(0, WIDTH)
                star_y = random.randint(-20, 0)  # Reset above the screen
            stars[i] = (star_x, star_y)
            pygame.draw.circle(screen, white, (star_x, star_y), 2)

        # Get keyboard input for player movement
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and user_x + 40 + user_speed <= WIDTH:
            user_x += user_speed
        if keys[K_LEFT] and user_x - 40 - user_speed >= 0:
            user_x -= user_speed

        # Move and draw obstacles
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed  # Move obstacle downward
            pygame.draw.rect(screen, red, (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))

            # Check for collision with player
            closest_x = max(obstacle[0], min(user_x, obstacle[0] + obstacle[2]))
            closest_y = max(obstacle[1], min(user_y, obstacle[1] + obstacle[3]))
            distance = ((user_x - closest_x) ** 2 + (user_y - closest_y) ** 2) ** 0.5

            if distance < 40:  # Player radius is 40
                game_over = True
                pygame.time.wait(2000) # Freeze 2 seconds after losing
                current_screen = 4  # Game Over screen
                break

            # Reset obstacle if it moves off-screen
            if obstacle[1] > HEIGHT:
                obstacle[0] = random.randint(0, WIDTH - obstacle[2])
                obstacle[1] = random.randint(-150, -50)  # Place it above the screen
                obstacles_dodged += 1

        # Check if the player has dodged enough obstacles to win
        if obstacles_dodged >= game_won_num:
            obstacles.clear()
            user_speed = 0
            sun_y += 0.5  # Move sun onto screen
            if sun_y >= HEIGHT // 2:
                pygame.time.wait(1000)
                current_screen = 5 # Switch to win screen

        # Increase speed periodically
        if pygame.time.get_ticks() - last_speed_increase >= 7500:
            obstacle_speed += 0.12 # Increase obstacle speed every 7.5 seconds
            last_speed_increase = pygame.time.get_ticks()

    # Game over screen
    elif current_screen == 4:
        screen.fill(black)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(restart_text, restart_rect)
    
    # Game won screen
    elif current_screen == 5:
        screen.fill(black)
        screen.blit(win_text, win_rect)
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()
