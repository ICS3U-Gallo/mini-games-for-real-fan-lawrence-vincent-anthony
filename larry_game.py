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
    {"id": 0, "type": "dialogue", "text": "Light."},
    {"id": 1, "type": "dialogue", "scene": "soil", "text": "Underneath the suffocating soil, you can make out a light gleaming from above."},
    {"id": 2, "type": "dialogue", "scene": "soil_light", "text": "Your bones creak as you burrow up, an ode to your antiquity."},
    {"id": 3, "type": "dialogue", "scene": "soil_light", "text": "The light becomes brighter the further up you crawl."},
    {"id": 4, "type": "dialogue", "scene": "emerge", "text": "Finally, you escape the earth's confines."},
    {"id": 5, "type": "dialogue", "scene": "wasteland", "text": "An atrocious landscape greets you. The year is 2078."},
    {"id": 6, "type": "dialogue","scene": "wasteland", "text": "Due to corporate greed and intercontinental warfare, the earth has become a deserted wasteland."},
    {"id": 7, "type": "dialogue", "scene": "wasteland","text": "Far too many cow farts in the ozone layer have trapped the Sun's immense heat onto earth, making survival a near impossible feat for the earth dwellers."},
    {"id": 8, "type": "dialogue", "scene": "city_ruins", "text": "You spot ruins of a city nearby."},
    {"id": 9, "type": "choice", "scene": "city_ruins", "options": [
        {"text": "Check out the city ruins", "next_line": 14},
        {"text": "Ignore the ruins and move on", "next_line": 10}
    ]},

    {"id": 10, "type": "dialogue", "scene": "journey_begin", "text": "With determination in your heart, you set off on your journey."},
    {"id": 11, "type": "dialogue", "scene": "journey_begin", "text": "The barren wasteland stretches before you, a reminder of the stakes."},
    {"id": 12, "type": "dialogue", "scene": "journey_begin", "text": "You take your first step towards fulfilling the prophecy, and the future of the world hinges on your actions."},
    {"id": 13, "type": "ending", "scene": "journey_begin", "text": "To be continued..."},

    {"id": 14, "type": "dialogue", "scene": "vendor", "text": "You decided to check out the ruins."},
    {"id": 15, "type": "dialogue", "scene": "vendor", "text": "Hello young man, you seem to be in quite dire need of new clothes, would you like to check out my wares?", "next_line":13},
    {"id": 16, "type": "dialogue", "scene": "vendor", "text": "Not implemented"},
    {"id": 17, "type": "choice", "options": [
        {"text": "Yes", "next_line": 19},
        {"text": "No", "next_line": 18}
    ]},
    {"id": 18, "type": "dialogue", "scene": "vendor", "text": "“Here, take this with you at least…” acquired item: Dog"},
    {"id": 19, "type": "dialogue", "scene": "vendor", "text": "Here are my wares: Sun Stone, Radio, Milk."},
    {"id": 20, "type": "dialogue", "scene": "vendor", "text": "You purchased an item.", "next_line": 18},
    {"id": 21, "type": "dialogue", "scene": "proceed", "text": "You proceed onwards."},
    {"id": 22, "type": "dialogue", "scene": "well", "text": "You spot a well with a ladder leading down it. Do you check it out?"},
    {"id": 23, "type": "choice", "scene": "well", "options": [
        {"text": "Yes", "next_line": 20},
    ]},
    {"id": 24, "type": "dialogue", "scene": "ladder", "text": "You climb down the ladder."},
    {"id": 25, "type": "dialogue", "scene": "pipe", "text": "The metal is rusted from years of non-maintenance, and flakes of metal peel off, stabbing into your raw flesh."},
    {"id": 26, "type": "dialogue", "scene": "pipe", "text": "You have dropped into a sewage pipe. There are 3 paths that you can take. Where do you choose to go?"},
    {"id": 27, "type": "choice", "scene": "pipe", "options": [
        {"text": "Left", "next_line": 37},
        {"text": "Forward", "next_line": 41},
        {"text": "Right", "next_line": 28}
    ]},
    {"id": 28, "type": "dialogue", "scene": "tunnel_right_path", "text": "You decide to go right, the tunnel's cold air sending shivers down your spine."},
    {"id": 29, "type": "dialogue", "scene": "tunnel_right_path", "text": "The sound of dripping water echoes through the narrow passage, as you notice an eerie glow ahead."},
    {"id": 30, "type": "dialogue", "scene": "alien_encounter", "text": "You approach cautiously, the glow growing brighter. Suddenly, you find yourself face-to-face with an alien creature."},
    {"id": 31, "type": "dialogue", "scene": "alien_encounter", "text": "The alien has a sleek, metallic body with piercing eyes that seem to look right through you."},
    {"id": 32, "type": "dialogue", "scene": "alien_encounter", "text": "It tilts its head, examining you curiously before emitting a low, humming sound."},
    {"id": 33, "type": "dialogue", "scene": "run_away", "text": "You turn and sprint back towards the way you came, your heart pounding in your chest."},
    {"id": 34, "type": "dialogue", "scene": "run_away", "text": "You feel a sudden, intense heat behind you. The tunnel lights up as the alien fires a beam of energy."},
    {"id": 35, "type": "dialogue", "scene": "run_away", "text": "The last thing you see is a blinding flash of light. Everything goes silent."},
    {"id": 36, "type": "ending", "scene": "run_away", "text": "You have died. The alien's power was far beyond anything you could handle."},

    {"id": 37, "type": "dialogue", "scene": "left_path", "text": "You spot a body lying on the ground, you see him clutching something in his hand. A dim light emanates from it."},
    {"id": 38, "type": "dialogue", "scene": "left_path", "text": "You move closer to see what he is holding."},
    {"id": 39, "type": "dialogue", "scene": "left_path", "text": "Item acquired: Sunstone."},
    {"id": 40, "type": "dialogue", "scene": "back", "text": "You go back the way you came from."},
    {"id": 41, "type": "dialogue", "scene": "forward_path", "text": "You move on forward."},
    {"id": 42, "type": "dialogue", "scene": "forward_path", "text": "You spot a flickering light up ahead."},
    {"id": 43, "type": "dialogue", "scene": "metropolis", "text": "Voices echo across the pipe walls."},
    {"id": 44, "type": "dialogue", "scene": "metropolis", "text": "You make your way out of the pipe, and discover a thriving metropolis laid out in front of you."},
    {"id": 45, "type": "dialogue", "scene": "woman_approach", "text": "HEY YOU THERE!"},
    {"id": 46, "type": "dialogue", "scene": "woman_approach", "text": "You turn your face to see a gauntly dressed woman approaching you."},
    {"id": 47, "type": "dialogue", "scene": "woman_approach", "text": "WHO ARE YOU? I’VE NEVER SEEN YER ‘ROUND TOWN B’FORE, STATE YOUR NAME!"},
    {"id": 48, "type": "choice", "scene": "woman_approach", "options": [
        {"text": "Take out dog", "next_line": 38}
    ]},
    {"id": 49, "type": "dialogue", "scene": "woman_response", "text": "You say your name."},
    {"id": 50, "type": "dialogue", "scene": "dog_out", "text": "You take out the dog."},
    {"id": 51, "type": "dialogue", "scene": "woman_shock", "text": "The woman steps back."},
    {"id": 52, "type": "dialogue", "scene": "woman_shock", "text": "Is that… the dog of PROPHECY?!?!" },
    {"id": 53, "type": "dialogue", "scene": "woman_shock", "text": "Come with me… if that is truly the dog of prophecy you hold, then the fate of the world lies on your shoulders…!!"},
    {"id": 54, "type": "dialogue", "scene": "crowd_walk", "text": "You are led through a crowd of people and down a hallway."},
    {"id": 55, "type": "dialogue", "scene": "crowd_walk", "text": "People cast unfriendly glances your way."},
    {"id": 56, "type": "dialogue", "scene": "crowd_walk", "text": "You notice the soot covering their bodies."},
    {"id": 57, "type": "dialogue", "scene": "crowd_walk", "text": "With nowhere for factory fumes to escape to within the underground city, it seems the residents were suscepted to its filth."},
    {"id": 58, "type": "dialogue", "scene": "cavern", "text": "Eventually you are led to a large cavern."},
    {"id": 59, "type": "dialogue", "scene": "cavern", "text": "The walls are plated with thick steel slabs, and in the middle sits a giant rocket-like object."},
     {"id": 60, "type": "dialogue", "scene": "prophet", "text": "You see a figure sitting cross-legged next to the fire, their face obscured by a hood."},
    {"id": 61, "type": "dialogue", "scene": "prophet", "text": "They lift their head slowly, revealing eyes that seem to pierce into your soul."},
    {"id": 62, "type": "dialogue", "scene": "prophet", "text": "You’ve finally arrived. I was beginning to think the prophecies were false."},
    {"id": 63, "type": "dialogue", "scene": "prophet", "text": "The dog you carry is a symbol of the ancient world, the key to salvation."},
    {"id": 64, "type": "choice", "scene": "prophet", "options": [
        {"text": "Ask about the prophecy", "next_line": 65},
    ]},
    {"id": 65, "type": "dialogue", "scene": "prophecy_explanation", "text": "The prophecy speaks of a savior who will emerge when the world has lost hope."},
    {"id": 66, "type": "dialogue", "scene": "prophecy_explanation", "text": "They will be the bearer of a dog of legend, whose presence heralds a new beginning."},
    {"id": 67, "type": "dialogue", "scene": "prophecy_explanation", "text": "However, the journey to fulfill this prophecy is fraught with peril."},
    {"id": 68, "type": "dialogue", "scene": "prophecy_explanation", "text": "Many have tried and failed, consumed by the darkness of this desolate world."},
    {"id": 69, "type": "dialogue", "scene": "prophet_choice", "text": "Are you willing to take on this burden?"},
    {"id": 70, "type": "choice", "scene": "prophet_choice", "options": [
        {"text": "Accept the burden", "next_line": 71},
        {"text": "Refuse", "next_line": 99}  
    ]},
    {"id": 71, "type": "dialogue", "scene": "death_refuse", "text": "You refuse, stating that this is not your responsibility."},
    {"id": 72, "type": "dialogue", "scene": "death_refuse", "text": "The prophet's expression darkens. 'So be it. The world will continue its descent into ruin.'"},
    {"id": 73, "type": "dialogue", "scene": "death_refuse", "text": "As you turn to leave, the ground trembles violently."},
    {"id": 74, "type": "dialogue", "scene": "death_refuse", "text": "A fissure opens beneath your feet, swallowing you whole."},
    {"id": 75, "type": "dialogue", "scene": "death_refuse", "text": "The darkness consumes you, and everything fades away."},
    {"id": 76, "type": "ending", "scene": "death_refuse", "text": "You have met a grim end. Try again."},


    {"id": 77, "type": "dialogue", "scene": "accept_path", "text": "You nod solemnly, accepting the role bestowed upon you."},
    {"id": 78, "type": "dialogue", "scene": "accept_path", "text": "The prophet smiles weakly. 'Very well. The journey ahead will test your resolve.'"},
    {"id": 79, "type": "dialogue", "scene": "accept_path", "text": "The fate of this world now rests in your hands."},
    {"id": 80, "type": "dialogue", "scene": "quest_start", "text": "You are given a button, labelled 'Destroy the Sun'"},
    {"id": 81, "type": "dialogue", "scene": "quest_start", "text": "You press the button, and the sun explodes. THE END"},

current_line = 0
choice_active = False
current_scene = None
dialogue_box_y = 450
current_choices = []
current_data = dialogue_script [0]

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
    else:
        screen.fill(sky_blue)

# Define the function to handle choice selection
def handle_choice_selection(next_line):
    global current_line, choice_active, current_data
    current_line = next_line  # Update the current line to the selected choice's next_line
    current_data = dialogue_script[current_line]
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

def next_step():
    global current_line, state, current_data
    if not current_data.get("next_line"):
        current_line += 1    
    else:
        current_line = current_data.get("next_line")
        
    current_data = dialogue_script[current_line]
    if current_line >= len(dialogue_script):
        state = MENU
        current_line = 0
        

# Main Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == MENU:
            for button in menu_buttons:
                button.handle_event(event)

        elif state == GAME:
            if current_data["type"]== "choice" and current_choices:
                for button in current_choices:
                    button.handle_event(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    next_step()
       
    if state == MENU:
        for button in menu_buttons:
            button.draw(screen)
    elif state == GAME:

        display_scene(screen, current_data.get("scene"))

        # Handle dialogue display
        if current_data["type"] == "dialogue":
            if not choice_active:
                display_dialogue(screen, current_data["text"])

        # Handle choice activation and display
        elif current_data["type"] == "choice" and not choice_active:
            choice_active = True
            set_choices(current_data["options"])  # Display choice buttons

        # Render choices if active
        if choice_active:
            for button in current_choices:
                button.draw(screen)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
