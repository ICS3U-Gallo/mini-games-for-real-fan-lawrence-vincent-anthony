import pygame
import pygame.freetype

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sun Quest")
clock = pygame.time.Clock()

sky_blue = (158, 240, 255)
button_color = (100, 200, 255)
hover_color = (50, 150, 200)
text_color = (0, 0, 0)

GAME_FONT = pygame.freetype.Font(None, 20)
SPEECH_FONT = pygame.freetype.Font(None, 9)

MENU = "menu"
GAME = "game"
CREDITS = "credits"
state = MENU

dialogue_script = [
    {"type": "dialogue", "text": "Light."},
    {"type": "dialogue", "text": "Underneath the suffocating soil, you can make out a light gleaming from above."},
    {"type": "dialogue", "text": "Your bones creak as you burrow up, an ode to your antiquity."},
    {"type": "dialogue", "text": "The light becomes brighter the further up you crawl."},
    {"type": "dialogue", "text": "Finally, you escape the earth's confines."},
    {"type": "dialogue", "text": "An atrocious landscape greets you."},
    {"type": "dialogue", "text": "The year is 2078."},
    {"type": "dialogue", "text": "Due to corporate greed and intercontinental warfare, the earth has become a deserted wasteland."},
    {"type": "dialogue", "text": "Far too many cow farts in the ozone layer have trapped the Sun's immense heat onto earth, making survival a near impossible feat for the earth dwellers."},
    {"type": "choice", "options": [
        {"text": "Check out the city ruins", "next_line": 11},
        {"text": "Ignore the ruins and move on", "next_line": 12}
    ]},
    {"type": "dialogue", "text": "You decided to check out the ruins."},
    {"type": "dialogue", "text": "You proceed onwards."},
    {"type": "dialogue", "text": "Hello young man, you seem to be in quite dire need of new clothes, would you like to check out my wares?"},
    {"type": "choice", "options": [
        {"text": "Yes", "next_line": 14},
        {"text": "No", "next_line": 17}
    ]},
    {"type": "dialogue", "text": "Here are my wares: Sun Stone, Radio, Milk."},
    {"type": "dialogue", "text": "You purchased an item."},
    {"type": "dialogue", "text": "You proceed onwards."},
    {"type": "dialogue", "text": "“Here, take this with you at least…” acquired item: Dog"},
    {"type": "dialogue", "text": "You proceed onwards."},
    {"type": "dialogue", "text": "You spot a well with a ladder leading down it. Do you check it out?"},
    {"type": "choice", "options": [
        {"text": "Yes", "next_line": 21},
        {"text": "No", "next_line": 22}
    ]},
    {"type": "dialogue", "text": "You climb down the ladder."},
    {"type": "dialogue", "text": "The metal is rusted from years of non-maintenance, and flakes of metal peel off, stabbing into your raw flesh."},
    {"type": "dialogue", "text": "You have dropped into a sewage pipe. There are 3 paths that you can take. Where do you choose to go?"},
    {"type": "choice", "options": [
        {"text": "Left", "next_line": 25},
        {"text": "Forward", "next_line": 29},
        {"text": "Right", "next_line": 32}
    ]},
    {"type": "dialogue", "text": "You spot a body lying on the ground, you see him clutching something in his hand. A dim light emanates from it."},
    {"type": "dialogue", "text": "You move closer to see what he is holding."},
    {"type": "dialogue", "text": "Item acquired: Sunstone."},
    {"type": "dialogue", "text": "You go back the way you came from."},
    {"type": "dialogue", "text": "You move on forward."},
    {"type": "dialogue", "text": "You spot a flickering light up ahead."},
    {"type": "dialogue", "text": "Voices echo across the pipe walls."},
    {"type": "dialogue", "text": "You make your way out of the pipe, and discover a thriving metropolis laid out in front of you."},
    {"type": "dialogue", "text": "HEY YOU THERE!"},
    {"type": "dialogue", "text": "You turn your face to see a gauntly dressed woman approaching you."},
    {"type": "dialogue", "text": "WHO ARE YOU? I’VE NEVER SEEN YER ‘ROUND TOWN B’FORE, STATE YOUR NAME!"},
    {"type": "choice", "options": [
        {"text": "Ignore her", "next_line": 37},
        {"text": "Take out dog", "next_line": 38}
    ]},
    {"type": "dialogue", "text": "You choose to ignore her."},
    {"type": "dialogue", "text": "You take out the dog."},
    {"type": "dialogue", "text": "The woman looks shocked and steps back."}
]

current_line = 0
choice_index = 0
choice_active = False
current_choices = []

class Button:
    def __init__(self, text, pos, size, callback):
        self.text = text
        self.pos = pos
        self.size = size
        self.callback = callback
        self.rect = pygame.Rect(pos, size)
        self.hovered = False

    def draw(self, screen):
        color = hover_color if self.hovered else button_color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        GAME_FONT.render_to(screen, (self.pos[0] + 20, self.pos[1] + 10), self.text, text_color)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.callback()

menu_buttons = []

def start_game():
    global state, current_line, choice_active
    state = GAME
    current_line = 0
    choice_active = False

def show_credits():
    global state
    state = CREDITS

def quit_game():
    pygame.quit()
    exit()

menu_buttons.append(Button("Start", (300, 200), (200, 50), start_game))
menu_buttons.append(Button("Credits", (300, 300), (200, 50), show_credits))
menu_buttons.append(Button("Quit", (300, 400), (200, 50), quit_game))

def display_dialogue(screen, text):
    screen.fill(sky_blue)
    SPEECH_FONT.render_to(screen, (50, 275), text, text_color)

def set_choices(options):
    global current_choices
    current_choices = []
    y_offset = 300
    for option in options:
        button = Button(option["text"], (250, y_offset), (300, 50),
                        lambda next_line=option["next_line"]: handle_choice_selection(next_line))
        current_choices.append(button)
        y_offset += 70

def handle_choice_selection(next_line):
    global current_line, choice_active
    current_line = next_line
    choice_active = False
    current_choices.clear()

def display_credits(screen):
    screen.fill(sky_blue)
    GAME_FONT.render_to(screen, (250, 250), "Credits: Game by Lawrence", text_color)
    GAME_FONT.render_to(screen, (250, 300), "Press SPACE to return", text_color)

running = True
while running:
    screen.fill(sky_blue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            for button in menu_buttons:
                button.handle_event(event)

        elif state == GAME:
            current_data = dialogue_script[current_line]

            if current_data["type"] == "choice" and not choice_active:
                choice_active = True
                set_choices(current_data["options"])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not choice_active:
                    current_line += 1
                    if current_line >= len(dialogue_script):
                        state = MENU  
                        current_line = 0 


                elif state == CREDITS and event.key == pygame.K_SPACE:
                    state = MENU

        elif state == CREDITS:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = MENU

        if choice_active:
            for button in current_choices:
                button.handle_event(event)

    if state == MENU:
        for button in menu_buttons:
            button.draw(screen)

    elif state == GAME:
        if choice_active:
            for button in current_choices:
                button.draw(screen)
        else:
            display_dialogue(screen, dialogue_script[current_line]["text"])

    elif state == CREDITS:
        display_credits(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
