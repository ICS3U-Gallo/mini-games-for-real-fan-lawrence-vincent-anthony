import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

BALL_RADIUS = 8
ball_speed_x = 4
ball_speed_y = -4
ball_speed_x = 7
ball_speed_y = -7
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)

paddle_width = 80
paddle_height = 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_height)

BRICK_WIDTH = 60
BRICK_HEIGHT = 20
initial_bricks = 9 * 5
bricks = [pygame.Rect(10 + i * (BRICK_WIDTH + 10), 10 + j * (BRICK_HEIGHT + 10), BRICK_WIDTH, BRICK_HEIGHT)
          for i in range(9) for j in range(5)]
stars = []
for _ in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    stars.append((x, y))

score = 0
font = pygame.font.Font(None, 36)
game_over = False
win = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over and not win:
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed_x *= -1
        if ball.top <= 0:
            ball_speed_y *= -1
        if ball.bottom >= HEIGHT: 
            game_over = True  

        if ball.colliderect(paddle):
            ball_speed_y *= -1

        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_speed_y *= -1
                score += 1
                break

        if not bricks:
            win = True

        mouse_x, _ = pygame.mouse.get_pos()
        paddle.centerx = mouse_x
        paddle.clamp_ip(screen.get_rect())

        screen.fill((0, 0, 0)) 
        pygame.draw.rect(screen, (225, 225, 225), paddle) 
        pygame.draw.ellipse(screen, (0, 225, 0), ball) 

        # Calculate background color based on the number of bricks remaining
        day_progress = 255 * (1 - len(bricks) / initial_bricks)
        background_color = (day_progress // 2, day_progress // 2, day_progress)
        sun_y = HEIGHT - int((day_progress / 255) * HEIGHT)
   
        screen.fill(background_color)
        pygame.draw.circle(screen, (255, 223, 0), (WIDTH // 2, sun_y), 50)
        pygame.draw.rect(screen, (225, 225, 225), paddle)
        pygame.draw.ellipse(screen, (0, 225, 0), ball)
        star_alpha = max(0, 255 - day_progress)  
        for x, y in stars:
            pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))
            star_surface = pygame.Surface((2, 2))
            star_surface.fill((255, 255, 255))
            star_surface.set_alpha(star_alpha)
            screen.blit(star_surface, (x, y))

        for brick in bricks:
            pygame.draw.rect(screen, (225, 0, 0), brick)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
        screen.fill((0, 0, 0))
        if game_over:
            end_text = font.render("Game Over!", True, (255, 0, 0))
            end_text = font.render("Game Over! You are unable to free the Sun", True, (255, 0, 0))
        elif win:
            end_text = font.render("You Win!", True, (0, 255, 0))
            end_text = font.render("You Win! You have freed the Sun! ", True, (0, 255, 0))
        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
