import pygame
from pathlib import Path


class Menu:

    def __init__(self, game_state, bg_path="./assets/images/tmp_background.png"):
        self.buttons = []
        self.game = game_state
        self.width, self.height = game_state.main_display.get_size()
        background_location = Path(bg_path)
        try:
            background_file = open(background_location, mode="rb")
        except FileNotFoundError:
            background_file = None
            print("Error: Missing main menu picture! Is the assets folder missing or path incorrect?"
                  "\nPATH={}".format(background_location))
            exit(-1)
        self.menu = pygame.image.load(background_file)
        self.menu = pygame.transform.scale(self.menu, self.game.main_display.get_size())
        self.update()

    # Draws the button again
    def update(self):
        for button in self.buttons:
            text = button.get_surf()
            gx, gy = self.game.main_display.get_size()
            button.rect = self.menu.blit(text, (gx * button.rel_x - button.width / 2,
                                                gy * button.rel_y - button.height / 2))
        self.game.main_display.blit(self.menu, (0, 0))

    # Adds a button to the menu and updates the menu
    def add_button(self, button):
        self.buttons.append(button)
        self.update()

    # Returns the name of a button in the menu if it is clicked
    def is_clicked(self):
        for event in self.game.event_queue:
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        return button.name
            # REMOVE EVENT FROM QUEUE

    # Returns all clicked buttons if that's even useful
    def all_clicked(self):
        events = []
        for event in self.game.event_queue:
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        events.append(button.name)
            # REMOVE EVENT FROM QUEUE
        return events


class MainMenu(Menu):

    def __init__(self, game_state):
        self.buttons = []
        self.game = game_state
        self.width, self.height = game_state.main_display.get_size()
        background_location = Path("./assets/images/tmp_background.png")
        logo_location = Path("./assets/images/Logo.png")
        try:
            background_file = open(background_location, mode="rb")
            logo_file = open(logo_location, mode="rb")
        except FileNotFoundError:
            background_file = None
            logo_file = None
            print("Error: Missing main menu picture! Is the assets folder missing or path incorrect?")
            exit(-1)
        self.menu = pygame.image.load(background_file)
        dim1 = self.menu.get_size()
        logo = pygame.image.load(logo_file)
        self.menu = pygame.transform.scale(self.menu, self.game.main_display.get_size())
        scalex, scaley = dim1[0] / self.menu.get_size()[0], dim1[1] / self.menu.get_size()[1]
        logo = pygame.transform.scale(logo, (int(scalex * logo.get_size()[0]), int(scaley * logo.get_size()[1])))
        # self.menu = pygame.Surface((width, height))

        self.buttons.append(Button("New_Game", 0.5, 0.5, 100, 50, "New Game"))
        self.buttons.append(Button("Continue", 0.5, 0.55, 100, 50, "Continue"))
        self.buttons.append(Button("Quit", 0.5, 0.6, 100, 50, "Quit"))

        self.update()
        gx, gy = self.menu.get_size()
        self.game.main_display.blit(logo, (gx/2 - logo.get_size()[0] / 2, gy / 3 - logo.get_size()[1]))

class Button:

    def __init__(self, name, rel_x, rel_y, width, height, text="", button_colour=(255, 255, 255), border_colour=(0,0,0)) :
        self.button_colour = button_colour
        self.border_colour = border_colour
        self.name = name
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.text = text
        pygame.font.init()
        self.font = pygame.font.SysFont("arial",50)
        text_width = pygame.font.Font.size(self.font, self.text)[0]
        if text_width < width:
            self.width = text_width
        else:
            self.width = width
        self.height = height

    def get_surf(self):
        surf = self.font.render(self.text, False, self.button_colour, (0, 0, 0))
        return pygame.transform.scale(surf, (self.width, self.height))
