import pygame
from pathlib import Path


class Menu:
    def __init__(self, game_state, bg_path="./assets/images/tmp_background.png"):
        self.buttons = []
        self.game = game_state
        self.width, self.height = game_state.main_display.get_size()
        self.menu_sprites = pygame.sprite.Group()
        background_location = Path(bg_path)
        try:
            background_file = open(background_location, mode="rb")
        except FileNotFoundError:
            background_file = None
            print("Error: Missing main menu picture! Is the assets folder missing or path incorrect?"
                  "\nPATH={}".format(background_location))
            exit(-1)
        self.menu = pygame.Surface.convert(pygame.image.load(background_file))
        self.original_dim = self.menu.get_size()
        self.menu = pygame.transform.scale(self.menu, self.game.main_display.get_size())
        self.update()

    # Draws the button again
    def update(self):
        for button in self.buttons:
            gx, gy = self.game.main_display.get_size()
            button.rect.center = (gx * button.rel_x, gy * button.rel_y)
            print(button.rect.center)
        self.menu_sprites.update()
        self.menu_sprites.draw(self.menu)
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
        super().__init__(game_state)
        logo_location = Path("./assets/images/Logo.png")
        try:
            logo_file = open(logo_location, mode="rb")
        except FileNotFoundError:
            logo_file = None
            print("Error: Missing logo picture! Is the assets folder missing or path incorrect?")
            exit(-1)
        logo = pygame.Surface.convert(pygame.image.load(logo_file))
        scalex, scaley = self.original_dim[0] / self.menu.get_size()[0], self.original_dim[1] / self.menu.get_size()[1]
        logo = pygame.transform.scale(logo, (int(scalex * logo.get_size()[0]), int(scaley * logo.get_size()[1])))

        self.buttons.append(ButtonSprite("New_Game", 0.5, 0.5, 400, 50, "New Game", (255, 0, 0), (255, 255, 0)))
        self.buttons.append(ButtonSprite("Continue", 0.5, 0.6, 400, 50, "Continue", (0, 0, 255), (0, 255, 0)))
        self.buttons.append(ButtonSprite("Quit", 0.5, 0.7, 400, 50, "Quit", (255, 0, 255), (0, 255, 255)))
        for sprite in self.buttons:
            self.menu_sprites.add(sprite)

        gx, gy = self.menu.get_size()
        self.menu.blit(logo, (gx/2 - logo.get_size()[0] / 2, gy / 3 - logo.get_size()[1]))
        self.update()


class ContinueMenu(Menu):
    def __init__(self, game_state):
        super().__init__(game_state)
        # self.menu = pygame.Surface((width, height))
        self.buttons = []

        self.buttons.append(ButtonSprite("Back", 0.5, 0.7, 400, 50, "Back", (255, 0, 255), (0, 255, 255)))
        save_path = Path('./saves').glob('**/*')
        saves = [x for x in save_path if x.is_file()]
        for i in range(len(saves)):
            self.buttons.append(ButtonSprite(saves[i], 0.5, 0.1 + 0.1 * i, 400, 50, "SAVE{}".format(i), (255, 0, 255), (0, 255, 255)))
        for sprite in self.buttons:
            self.menu_sprites.add(sprite)

        self.update()


class ButtonSprite(pygame.sprite.Sprite):
    def __init__(self, name, rel_x, rel_y, width, height, text="", button_colour=(255, 255, 255), text_colour=(0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.button_colour = button_colour
        self.text_colour = text_colour
        self.name = name
        self.rel_x = rel_x
        self.rel_y = rel_y
        self.text = " " + text + " "
        pygame.font.init()
        self.font = pygame.font.SysFont("impact", width // len(self.text))
        self.image = self.font.render(self.text, False, self.button_colour, self.text_colour)
        self.rect = self.image.get_rect()
