import pygame
import random

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

BALL_RADIUS = 8
ball_speed_x = 7
ball_speed_y = -7

balls = [pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)]
ball_speeds = [(ball_speed_x, ball_speed_y)]

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

sun_y = 50

first_row_bricks = [brick for brick in bricks if brick.y == 130]
multi_ball_box = random.choice(first_row_bricks)

power_up_spawned = False
power_up = None 
paddle_expanded = False
paddle_timer = 0 
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
        for i, ball in enumerate(balls):
            ball.x += ball_speeds[i][0]
            ball.y += ball_speeds[i][1]

            if ball.left <= 0 or ball.right >= WIDTH:
                ball_speeds[i] = (-ball_speeds[i][0], ball_speeds[i][1])
            if ball.top <= 0:
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])
            if ball.bottom >= HEIGHT:
                balls.pop(i)
                ball_speeds.pop(i)
                if len(balls) == 0:
                    game_over = True
                break

            if ball.colliderect(paddle):
                ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])

            for brick in bricks[:]:
                if ball.colliderect(brick):
                    bricks.remove(brick)
                    ball_speeds[i] = (ball_speeds[i][0], -ball_speeds[i][1])
                    score += 1

                    if not power_up_spawned and random.random() < 0.2:
                        power_up_spawned = True
                        power_up = pygame.Rect(brick.x,brick.y,20,20)
                    if brick == multi_ball_box:
                        for _ in range(2):
                            new_ball = pygame.Rect(ball.x, ball.y, BALL_RADIUS * 2, BALL_RADIUS * 2)
                            new_speed_x = random.choice([-7, 7])
                            new_speed_y = random.choice([-7, 7])
                            balls.append(new_ball)
                            ball_speeds.append((new_speed_x, new_speed_y))
                    break

        if not bricks:
            win = True

        mouse_x, _ = pygame.mouse.get_pos()
        paddle.centerx = mouse_x
        paddle.clamp_ip(screen.get_rect())

        day_progress = 255 * (1 - len(bricks) / initial_bricks)
        background_color = (day_progress // 2, day_progress // 2, day_progress)
        screen.fill(background_color)
        if power_up:
            power_up.y += 3 
            if power_up.colliderect(paddle):
                paddle.width = 120  
                paddle_expanded = True
                paddle_timer = pygame.time.get_ticks()  
                power_up = None  
                power_up_spawned = False

        if paddle_expanded and pygame.time.get_ticks() - paddle_timer > 5000:
            paddle.width = 80  
            paddle_expanded = False

        
        pygame.draw.circle(screen, (255, 223, 0), (WIDTH // 2, sun_y), 50)

        star_alpha = max(0, 255 - day_progress)
        for x, y in stars:
            star_surface = pygame.Surface((2, 2))
            star_surface.fill((255, 255, 255))
            star_surface.set_alpha(star_alpha)
            screen.blit(star_surface, (x, y))

        for ball in balls:
            pygame.draw.ellipse(screen, (225, 225, 0), ball)

        pygame.draw.rect(screen, (225, 225, 225), paddle)

        for brick in bricks:
            color = (0, 0, 255) if brick == multi_ball_box else (225, 0, 0)
            pygame.draw.rect(screen, color, brick)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (5, 5))

    else:
        screen.fill((0, 0, 0))
        if game_over:
            end_text = font.render("Game Over! You are unable to free the Sun", True, (255, 0, 0))
        elif win:
            end_text = font.render("You Win! You have freed the Sun!", True, (0, 255, 0))
            pygame.draw.circle(screen, (255, 223, 0), (WIDTH // 2, sun_y+50), 50)
            screen.fill(background_color)
        screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - end_text.get_height() // 2))


    pygame.display.flip()
    clock.tick(30)

pygame.quit()
