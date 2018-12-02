import pygame
from pathlib import Path


class Menu:

    def __init__(self, width, height, game_state):
        self.buttons = []
        self.game = game_state
        self.width = width
        self.height = height
        background_location = Path("./assets/images/tmp_background.png")
        try:
            background_file = open(background_location, mode="rb")
        except FileNotFoundError:
            background_file = None
            print("Error: Missing splash screen picture! Is the assets folder missing or path incorrect?")
            exit(-1)
        self.menu = pygame.image.load(background_file)

    def update(self):
        for button in self.buttons:
            (rect, text) = button.get_rect(self.width, self.height)
            sx, sy = rect.center
            gx, gy = self.menu.get_rect().center
            self.menu.blit(rect, (gx-sx, gy-sy))
            self.menu.blit(text, (gx-sx, gy-sy))


class Button:

    def __init__(self, rel_x, rel_y, width, height, button_colour = (255,255,255), border_colour=(0,0,0), text="") :
        self.button_colour = button_colour
        self.border_colour = border_colour
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.text = text
        self.font = pygame.font("Arial")
        text_width = self.pygame.font.Font.size(self.font, self.text)
        if text_width < width:
            self.width = text_width
        else:
            self.width = width
        self.height = height

    def get_rect(self, screen_width, screen_height):
        dimensions = (self.rel_x * screen_width - self.width / 2, self.rel_y * screen_height - self.height / 2,
                      self.width, self.height)
        return pygame.Rect(dimensions), self.font.render(self.text, False, self.border_colour)

