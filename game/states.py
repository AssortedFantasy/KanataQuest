import pygame as pg
from . import menus
from collections import deque
# States.py is the definition file for game states!
# main_loops must be run in a game state.

# GLOBAL PARAMETERS
default_fps = 30
default_res = 640, 480
default_display_params = pg.RESIZABLE
default_background_colour = (255, 255, 255)  # White


class KeyBindings:
    def __init__(self):
        self.up = [pg.K_UP, pg.K_w]
        self.down = [pg.K_DOWN, pg.K_d]
        self.left = [pg.K_LEFT, pg.K_a]
        self.right = [pg.K_RIGHT, pg.K_d]
        self.inventory = [pg.K_e]
        self.select = [pg.K_RETURN]
        self.go_back = [pg.K_ESCAPE]


class GameState:
    """
    GameState is large file which serves to hold everything that is relevant to the game and running it.
    It serves to fill the function of not having huge numbers of global variables littered literally everywhere.
    """
    def __init__(self):
        self.is_running = True
        self.event_queue = deque()

        # Have to do with display scaling
        self.background = default_background_colour
        self.res = default_res
        self.screen_res_out_of_date = True
        self.display_params = default_display_params
        self.main_display = pg.Surface(self.res)
        self.display_rect = self.main_display.get_rect()

        self.menu = []
        self.current_state = "MENU"

        self.fps = default_fps   # Probably don't set to 0
        self.clock = pg.time.Clock()  # Clock object for this game state

    def fix_screen_resolution(self, force=False):
        # Note this actually wipes the screen!
        if self.screen_res_out_of_date or force:
            self.res = pg.display.get_surface().get_rect().size
            self.main_display = pg.Surface(self.res)
            self.display_rect = self.main_display.get_rect()
            self.main_display.fill(self.background)
            return True
        return False

    # TODO: MOVE MENU CODE HERE
    def update(self):
        if self.current_state == "MENU":
            self.menu.append(menus.MainMenu(self))
            self.current_state = "MENU_DEFINED"
        elif self.current_state == "MENU_DEFINED":
            button_press = self.menu[-1].is_clicked()
            if button_press == "Quit":
                pg.event.post(pg.event.Event(pg.QUIT, {}))

            elif button_press == "New_Game":
                print("TODO: IMPLEMENT NEW_GAME")
                # New game should just start the game, no menu required
                # This state should generate a save and then converge with continue menu
                self.current_state = "NEW_GAME_MENU"

            elif button_press == "Continue":
                self.menu.append(menus.ContinueMenu(self))
                self.current_state = "CONTINUE_MENU"

        elif self.current_state == "CONTINUE_MENU":
            button_press = self.menu[-1].is_clicked()
            if button_press == "Back":
                self.menu.pop()
                self.current_state = "MENU"
            elif button_press:
                print(button_press)
                # LOAD FILE
        elif self.current_state == "NEW_GAME_MENU":
            self.menu.append(menus.NewGameMenu(self))

