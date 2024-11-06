import pygame
import random

pygame.init()

# Screen dimensions
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Global vairables 
BALL_RADIUS = 8
ball_speed_x = 4
ball_speed_y = -4
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)

paddle_width = 80
paddle_height = 10
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 30, paddle_width, paddle_height)

BRICK_WIDTH = 60
BRICK_HEIGHT = 20
bricks = [pygame.Rect(10 + i * (BRICK_WIDTH + 10), 10 + j * (BRICK_HEIGHT + 10), BRICK_WIDTH, BRICK_HEIGHT)
          for i in range(9) for j in range(5)]
stars = []
for _ in range(100):
    x = random.randrange(0, WIDTH)
    y = random.randrange(0, HEIGHT)
    stars.append((x, y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game State Updates
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # when the ball hits side walls or ceiling 
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
        # when the ball misses the paddle
    if ball.bottom >= HEIGHT: 
        print("Game Over!")
        running = False  

    # when the ball hits the paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # when ball hits bricks 
    for brick in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y *= -1
            break

    # Drawing
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (225, 225, 225), paddle) 
    pygame.draw.ellipse(screen, (0, 225, 0), ball) 

    # Draw stars
    for x, y in stars:
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 2, 2))

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, (225, 0, 0), brick)

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()



