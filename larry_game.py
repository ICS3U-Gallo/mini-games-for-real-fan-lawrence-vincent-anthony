import pygame
import pygame.freetype 

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

sky_blue = (158, 240, 255)

GAME_FONT = pygame.freetype.Font(None, 24)
running =  True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(sky_blue)
    GAME_FONT.render_to(screen, (300, 275), "Welcome to Sun Quest!", (0, 0, 0))

    pygame.display.flip()
    clock.tick(60)/1000

pygame.quit()
