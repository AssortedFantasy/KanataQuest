import pygame as pg
# States.py is the definition file for game states!
# main_loops must be run in a game state.

# GLOBAL PARAMETERS
default_fps = 30
default_res = 640, 480
default_display_params = pg.RESIZABLE | 0
default_background_colour = (255, 255, 255)  # White


class Settings:
    def __init__(self):
        self.up = [pg.K]
        self.down = []
        self.left = []
        self.right = []
        self.inventory = []
        self.select = []
        self.go_back = []


class GameState:
    """
    GameState is large file which serves to hold everything that is relevant to the game and running it.
    It serves to fill the function of not having huge numbers of global variables littered literally everywhere.
    """
    def __init__(self):
        self.is_active = True
        self.is_running = True

        self.current_state = "MENU"

        self.background = default_background_colour  # Background colour
        self.res = default_res  # Width , Height
        self.screen_res_out_of_date = True
        self.display_params = default_display_params
        self.main_display = pg.Surface(self.res)
        self.display_rect = self.main_display.get_rect()

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
