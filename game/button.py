import pygame

class Menu:

    def __init__(self, width, height, game_state):
        self.buttons = []
        self.game = game_state
        self.width = width
        self.height = height

    def draw_buttons(self):
        for button in self.buttons:
            (rect, text) = button.get_rect(self.width, self.height)
            self.game.main_display.blit()

class Button:

    def __init__(self, rel_x, rel_y, width, height, game_state, button_colour = (255,255,255), border_colour=(0,0,0), text="") :
        self.button_colour = button_colour
        self.border_colour = border_colour
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.text = text
        self.font = pygame.font("Arial")
        text_width =  self.pygame.font.Font.size(self.font, self.text)
        if text_width < width:
            self.width = text_width
        else:
            self.width = width
        self.height = height

    def get_rect(self, screen_width, screen_height):
        width = self.width / 2
        height = self.height / 2
        dimensions = (self.rel_x * screen_width - width, self.rel_y * screen_height - height, width * 2, height * 2)
        return pygame.Rect(dimensions), self.font.render(self.text, False, self.border_colour)

