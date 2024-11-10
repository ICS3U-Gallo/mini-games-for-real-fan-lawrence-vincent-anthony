import pygame, sys
import pygame.freetype 
from pygame.sprite import Sprite
from pygame.rect import Rect

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sun Quest Menu")
clock = pygame.time.Clock()

sky_blue = (158, 240, 255)
button_color = (100, 200, 255)
hover_color = (50, 150, 200)
text_color = (0, 0, 0)

GAME_FONT = pygame.freetype.Font(None, 36)

buttons = [
    {"text": "Start", "rect": pygame.Rect(300, 200, 200, 50), "action": "start"},
    {"text": "Credits", "rect": pygame.Rect(300, 300, 200, 50), "action": "credits"},
    {"text": "Quit", "rect": pygame.Rect(300, 400, 200, 50), "action": "quit"},
]

running = True
menu_active = True

def draw_button(screen, text, rect, is_hovered):
    color = hover_color if is_hovered else button_color
    pygame.draw.rect(screen, color, rect)
    GAME_FONT.render_to(screen, (rect.x + 20, rect.y + 10), text, text_color)

while running:
    screen.fill(sky_blue)
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if menu_active:
        for button in buttons:
            is_hovered = button["rect"].collidepoint(mouse_pos)
            draw_button(screen, button["text"], button["rect"], is_hovered)


            if is_hovered and mouse_click[0]: 
                if button["action"] == "start":
                    menu_active = False 
                elif button["action"] == "credits":
                    print("Credits: Game made by [Your Name]")
                elif button["action"] == "quit":
                    running = False

    pygame.display.flip()
    clock.tick(60)




screen = pygame.display.set_mode((1500, 1500))
clock = pygame.time.Clock()

sky_blue = (158, 240, 255)

GAME_FONT = pygame.freetype.Font(None, 14)

dialogue_lines = [
    "Light.",
    "Underneath the suffocating soil, you can make out a light gleaming from above.",
    "Your bones creak as you burrow up, an ode to your antiquity.",
    "The light becomes brighter the further up you crawl.",
    "Finally, you escape the earth's confines.",
    "An atrocious landscape greets you.",
    "The year is 2078.",
    "Due to corporate greed and intercontinental warfare, the earth has become a deserted wasteland.",
    "Far too many cow farts in the ozone layer have trapped the Sun's immense heat onto earth, making survival a near impossible feat for the earth dwellers.",
    "",
    "You spot what looks to be ruins of a city nearby. Do you go check it out?",
    "Hello young man, you seem to be in quite dire need of new clothes, would you like to check out my wares?",

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

    GAME_FONT.render_to(screen, (100, 975), dialogue_lines[current_line], (0, 0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
