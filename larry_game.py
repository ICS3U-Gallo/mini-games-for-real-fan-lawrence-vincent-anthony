import pygame
import pygame.freetype

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sun Quest")
clock = pygame.time.Clock()

# Colors
sky_blue = (158, 240, 255)
button_color = (100, 200, 255)
hover_color = (50, 150, 200)
text_color = (0, 0, 0)
dialogue_box_color = (200, 200, 200)
soil_color = (90, 60, 20)
light_color = (255, 255, 100)
wasteland_color = (170, 120, 60)
city_color = (80, 80, 80)
well_color = (100, 100, 120)

# Fonts
GAME_FONT = pygame.freetype.Font(None, 20)
SPEECH_FONT = pygame.freetype.Font(None, 16)

# Game States
MENU = "menu"
GAME = "game"
CREDITS = "credits"
state = MENU

# Dialogue Script with Scenes
dialogue_script = [
    {"type": "dialogue", "text": "Light."},
    {"type": "scene", "scene": "soil"},
    {"type": "dialogue", "text": "Underneath the suffocating soil, you can make out a light gleaming from above."},
    {"type": "scene", "scene": "soil_light"},
    {"type": "dialogue", "text": "Your bones creak as you burrow up, an ode to your antiquity."},
    {"type": "dialogue", "text": "The light becomes brighter the further up you crawl."},
    {"type": "scene", "scene": "emerge"},
    {"type": "dialogue", "text": "Finally, you escape the earth's confines."},
    {"type": "scene", "scene": "wasteland"},
    {"type": "dialogue", "text": "An atrocious landscape greets you. The year is 2078."},
    {"type": "dialogue", "text": "Due to corporate greed and intercontinental warfare, the earth has become a deserted wasteland."},
    {"type": "dialogue", "text": "Far too many cow farts in the ozone layer have trapped the Sun's immense heat onto earth, making survival a near impossible feat for the earth dwellers."},
    {"type": "scene", "scene": "city_ruins"},
    {"type": "dialogue", "text": "You spot ruins of a city nearby."},
    {"type": "choice", "options": [
        {"text": "Check out the city ruins", "next_line": 16},
        {"text": "Ignore the ruins and move on", "next_line": 17}
    ]},
    {"type": "scene", "scene": "vendor"},
    {"type": "dialogue", "text": "You decided to check out the ruins."},
    {"type": "dialogue", "text": "Hello young man, you seem to be in quite dire need of new clothes, would you like to check out my wares?"},
    {"type": "choice", "options": [
        {"text": "Yes", "next_line": 19},
        {"text": "No", "next_line": 22}
    ]},
    {"type": "dialogue", "text": "Here are my wares: Sun Stone, Radio, Milk."},
    {"type": "dialogue", "text": "You purchased an item."},
    {"type": "scene", "scene": "proceed"},
    {"type": "dialogue", "text": "You proceed onwards."},
    {"type": "dialogue", "text": "“Here, take this with you at least…” acquired item: Dog"},
    {"type": "scene", "scene": "well"},
    {"type": "dialogue", "text": "You spot a well with a ladder leading down it. Do you check it out?"},
    {"type": "choice", "options": [
        {"text": "Yes", "next_line": 26},
        {"text": "No", "next_line": 27}
    ]},
    {"type": "scene", "scene": "ladder"},
    {"type": "dialogue", "text": "You climb down the ladder."},
    {"type": "scene", "scene": "pipe"},
    {"type": "dialogue", "text": "The metal is rusted from years of non-maintenance, and flakes of metal peel off, stabbing into your raw flesh."},
    {"type": "dialogue", "text": "You have dropped into a sewage pipe. There are 3 paths that you can take. Where do you choose to go?"},
    {"type": "choice", "options": [
        {"text": "Left", "next_line": 30},
        {"text": "Forward", "next_line": 34},
        {"text": "Right", "next_line": 37}
    ]},
    {"type": "scene", "scene": "left_path"},
    {"type": "dialogue", "text": "You spot a body lying on the ground, you see him clutching something in his hand. A dim light emanates from it."},
    {"type": "dialogue", "text": "You move closer to see what he is holding."},
    {"type": "dialogue", "text": "Item acquired: Sunstone."},
    {"type": "scene", "scene": "back"},
    {"type": "dialogue", "text": "You go back the way you came from."},
    {"type": "scene", "scene": "forward_path"},
    {"type": "dialogue", "text": "You move on forward."},
    {"type": "dialogue", "text": "You spot a flickering light up ahead."},
    {"type": "scene", "scene": "metropolis"},
    {"type": "dialogue", "text": "Voices echo across the pipe walls."},
    {"type": "dialogue", "text": "You make your way out of the pipe, and discover a thriving metropolis laid out in front of you."},
    {"type": "scene", "scene": "woman_approach"},
    {"type": "dialogue", "text": "HEY YOU THERE!"},
    {"type": "dialogue", "text": "You turn your face to see a gauntly dressed woman approaching you."},
    {"type": "dialogue", "text": "WHO ARE YOU? I’VE NEVER SEEN YER ‘ROUND TOWN B’FORE, STATE YOUR NAME!"},
    {"type": "choice", "options": [
        {"text": "Ignore her", "next_line": 43},
        {"text": "Take out dog", "next_line": 44}
    ]},
    {"type": "dialogue", "text": "You choose to ignore her."},
    {"type": "scene", "scene": "dog"},
    {"type": "dialogue", "text": "You take out the dog."},
    {"type": "scene", "scene": "woman_shock"},
    {"type": "dialogue", "text": "The woman looks shocked and steps back."}
]

current_line = 0
choice_active = False
current_scene = None
dialogue_box_y = 450

# Menu Functions and Buttons
def start_game():
    global state, current_line
    state = GAME
    current_line = 0

def show_credits():
    global state
    state = CREDITS

def quit_game():
    pygame.quit()
    exit()

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

menu_buttons = [
    Button("Start", (300, 200), (200, 50), start_game),
    Button("Credits", (300, 300), (200, 50), show_credits),
    Button("Quit", (300, 400), (200, 50), quit_game)
]

# Scene Drawing Function
def display_scene(screen, scene):
    if scene == "soil":
        screen.fill(soil_color)
    elif scene == "soil_light":
        screen.fill(soil_color)
        pygame.draw.rect(screen, light_color, (350, 200, 100, 300))  # Light beam
    elif scene == "emerge":
        screen.fill(sky_blue)
        pygame.draw.rect(screen, soil_color, (0, 400, 800, 200))  # Ground
    elif scene == "wasteland":
        screen.fill(wasteland_color)
        pygame.draw.circle(screen, (255, 223, 0), (700, 100), 50)  # Sun
    elif scene == "city_ruins":
        screen.fill(sky_blue)
        for x in range(100, 700, 150):
            pygame.draw.rect(screen, city_color, (x, 300, 50, 300))  # Buildings
    elif scene == "vendor":
        screen.fill(sky_blue)
        pygame.draw.rect(screen, (150, 75, 0), (300, 400, 200, 100))  # Vendor's counter
    elif scene == "well":
        screen.fill(sky_blue)
        pygame.draw.circle(screen, well_color, (400, 300), 50)  # Well

# Define the function to handle choice selection
def handle_choice_selection(next_line):
    global current_line, choice_active
    current_line = next_line  # Update the current line to the selected choice's next_line
    choice_active = False  # Deactivate choices once a selection is made


# Display Dialogue Box
def display_dialogue_box(screen, text):
    pygame.draw.rect(screen, dialogue_box_color, (50, dialogue_box_y, 700, 130), border_radius=10)
    SPEECH_FONT.render_to(screen, (70, dialogue_box_y + 30), text, text_color)

def display_dialogue(screen, text):
    # Draw the dialogue box area
    dialogue_box = pygame.Rect(50, 450, 700, 100)
    pygame.draw.rect(screen, (50, 50, 50), dialogue_box, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), dialogue_box, 3)  # Outline of the box
    # Render the dialogue text inside the dialogue box
    SPEECH_FONT.render_to(screen, (70, 475), text, (255, 255, 255))

def set_choices(options):
    global current_choices, choice_active
    current_choices = []
    y_offset = 320
    for idx, option in enumerate(options):
        button = Button(
            text=option["text"],
            pos=(250, y_offset),
            size=(300, 50),
            callback=lambda idx=idx: handle_choice_selection(options[idx]["next_line"])
        )
        current_choices.append(button)
        y_offset += 70
    choice_active = True

# Main Loop
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_line += 1
                    if current_line >= len(dialogue_script):
                        state = MENU
                        current_line = 0

    if state == MENU:
        for button in menu_buttons:
            button.draw(screen)

    elif state == GAME:
        current_data = dialogue_script[current_line]

        # Display the scene first if it's a "scene" type
        if current_data["type"] == "scene":
            display_scene(screen, current_data["scene"])
            if not choice_active:  # Do not skip choice activation
                current_line += 1  # Move to the next line if not at a choice

        # Handle dialogue display
        elif current_data["type"] == "dialogue":
            display_scene(screen, current_scene)  # Keep current scene displayed
            if not choice_active:
                display_dialogue(screen, current_data["text"])

        # Handle choice activation and display
        elif current_data["type"] == "choice" and not choice_active:
            choice_active = True
            set_choices(current_data["options"])  # Display choice buttons

        # Event handling for SPACE key to proceed dialogue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not choice_active:
                current_line += 1
                if current_line >= len(dialogue_script):
                    state = MENU
                    current_line = 0

        # Render choices if active
        if choice_active:
            for button in current_choices:
                button.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
