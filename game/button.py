import pygame
from pathlib import Path


class Menu:

    def __init__(self, width, height, game_state):
        self.buttons = []
        self.game = game_state
        self.width = width
        self.height = height
        background_location = Path("./assets/images/tmp_background.png")
        logo_location = Path("./assets/images/Logo.png")
        try:
            background_file = open(background_location, mode="rb")
        except FileNotFoundError:
            background_file = None
            print("Error: Missing splash screen picture! Is the assets folder missing or path incorrect?")
            exit(-1)
        self.menu = pygame.image.load(background_file)
        self.menu = pygame.transform.scale(self.menu, (width, height))
        # self.menu = pygame.Surface((width, height))
        self.buttons.append(Button("Sample", 0.5, 0.5, 100, 50, "New Game"))
        self.update()
        print(self.is_clicked(pygame.mouse.get_pos()))

    def update(self):
        for button in self.buttons:
            text = button.get_rect(self.width, self.height)
            gx, gy = self.menu.get_rect().center
            button.rect = self.menu.blit(text, (gx, gy))  # Blit onto the same position as the rectangle
        self.game.main_display.blit(self.menu, (0, 0))

    def is_clicked(self, mos_pos):
        for button in self.buttons:
            if button.rect.collidepoint(mos_pos):
                return button.name

class Button:

    def __init__(self, name, rel_x, rel_y, width, height, text="", button_colour=(255, 255, 255), border_colour=(0,0,0)) :
        self.button_colour = button_colour
        self.border_colour = border_colour
        self.name = name
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.text = text
        pygame.font.init()
        self.font = pygame.font.SysFont("arial",20)
        text_width = pygame.font.Font.size(self.font, self.text)[0]
        if text_width < width:
            self.width = text_width
        else:
            self.width = width
        self.height = height

    def get_rect(self, screen_width, screen_height):
        return self.font.render(self.text, False, self.button_colour, (0, 0, 0))

