import pygame, sys
import pygame.freetype 

pygame.init()

screen = pygame.display.set_mode((1500, 1500))
clock = pygame.time.Clock()

sky_blue = (158, 240, 255)

AgmenaPro = 'Agmena Pro Book.ttf'

GAME_FONT = pygame.freetype.Font(AgmenaPro, 14)

dialogue_lines = [
    "Light.",
    "Underneath the suffocating soil, you can make out a light gleaming from above.",
    "Your bones creak as you burrow up, an ode to your antiquity.",
    "The light becomes brighter the further up you crawl.",
    "Finally, you escape the earth's confines.",
    "An atrocious landscape greets you.",
    "The year is 2078.",
    "Due to corporate greed and intercontinental warfare, the earth has become a deserted wasteland.",
    "Far too many cow farts in the ozone layer have trapped the Sun's immense heat onto earth, making survival a near impossible feat for the earth dwellers."
]
current_line = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if current_line < len(dialogue_lines) - 1:
                    current_line += 1
                else:
                    current_line = 0

    screen.fill(sky_blue)

    GAME_FONT.render_to(screen, (100, 275), dialogue_lines[current_line], (0, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
